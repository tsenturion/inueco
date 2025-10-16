import pytest
import math
from buggy_function2 import generate_students, compute_averages, filter_and_sort


class TestGenerateStudents:

    def test_generate_students_raises_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            generate_students(5)
    
    def test_generate_students_structure_with_mock(self):
        result = generate_students(0)
        assert isinstance(result, list)
class TestComputeAverages:
    @pytest.fixture
    def sample_students_fixed(self):

        return [
            {
                "id": 1,
                "scores": [80, 90, 100, 85, 95],
                "age": 20,
                "score": [80, 90, 100, 85, 95] 
            },
            {
                "id": 2, 
                "scores": [70, 85, 95, 80, 90],
                "age": 19,
                "score": [70, 85, 95, 80, 90]
            }
        ]
    
    def test_compute_averages_structure_with_fixed_data(self, sample_students_fixed):

        result = compute_averages(sample_students_fixed)
        
        assert isinstance(result, list)
        assert len(result) == len(sample_students_fixed)
        
        required_fields = ["id", "average", "age", "adjusted", "honor"]
        for item in result:
            for field in required_fields:
                assert field in item
    
    def test_compute_averages_zero_division_handling(self):

        problem_data = [
            {"id": 1, "scores": [80, 90], "age": 20},  
        ]
        
        with pytest.raises(ZeroDivisionError):
            compute_averages(problem_data)
    
    def test_compute_averages_type_issues(self, sample_students_fixed):

        result = compute_averages(sample_students_fixed)
        
        for item in result:
         
            assert isinstance(item["honor"], (bool, str))
            assert "extra_calc" in item
            assert isinstance(item["modifier"], (int, float, list))
    
    def test_compute_averages_none_scores_handling(self):

        test_data = [
            {"id": 1, "scores": None, "age": 20},  
        ]
        
        with pytest.raises(TypeError):
            compute_averages(test_data)


class TestFilterAndSort:
    @pytest.fixture
    def sample_averages_fixed(self):

        return [
            {"id": 1, "average": 85.0, "age": 22, "adjusted": 82, "final_score": 337},
            {"id": 2, "average": 92.0, "age": 19, "adjusted": 90, "final_score": 365},
            {"id": 3, "average": 78.0, "age": 25, "adjusted": 76, "final_score": 304},
        ]
    
    def test_filter_and_sort_logic_error_detection(self):

        test_data = [
            {"id": 1, "average": 85.0, "age": 22, "adjusted": 82},
            {"id": 2, "average": 92.0, "age": 19, "adjusted": 90},
        ]
        
        with pytest.raises(TypeError):
            filter_and_sort(test_data, 21, 85.0)
    
    def test_filter_and_sort_with_preprocessed_data(self, sample_averages_fixed):

        def mock_filter_and_sort(students, min_age, max_avg):
            filtered = []
            for s in students:
                if s.get("age", 0) >= min_age and s.get("average", 0) <= max_avg:
                    filtered.append(s)
                else:
                    filtered.append(s)  
            for s in filtered:
                try:
                    s["rank"] = math.floor(s.get("adjusted", 0) / 10)
                except:
                    s["rank"] 
            
            for s in filtered:
                s["extra_calc"] = str(s.get("final_score", 0)) + "string" 
            
            return filtered
        
        result = mock_filter_and_sort(sample_averages_fixed, 20, 90.0)
        
        assert len(result) == len(sample_averages_fixed)
        
        for item in result:
            assert "rank" in item
            assert isinstance(item["rank"], (int, str))
    
    def test_filter_and_sort_type_safety_issues(self):

        test_data = [
            {"id": 1, "average": 85.0, "age": 22, "adjusted": 82, "final_score": 337},
        ]
        
        with pytest.raises(TypeError):
            filter_and_sort(test_data, 18, 100.0)


class TestErrorHandling:
    def test_empty_input_handling(self):
        result_compute = compute_averages([])
        result_filter = filter_and_sort([], 18, 100.0)
        
        assert result_compute == []
        assert result_filter == []
    
    def test_missing_keys_handling(self):
        incomplete_data = [
            {"id": 1},  
        ]
        

        with pytest.raises(ZeroDivisionError):
            compute_averages(incomplete_data)
    
    def test_none_values_comparison_issue(self):
        problematic_data = [
            {"id": 1, "average": None, "age": 20, "adjusted": None},
        ]
        

        with pytest.raises(TypeError):
            filter_and_sort(problematic_data, 18, 100.0)


class TestDataTypesValidation:
    def test_expected_data_types_in_ideal_case(self):

        ideal_data = [
            {
                "id": 1, 
                "scores": [80, 90, 85], 
                "age": 20,
                "score": [80, 90, 85]  
            }
        ]
        
        result = compute_averages(ideal_data)
        
        assert isinstance(result, list)
        assert isinstance(result[0]["id"], int)
        assert isinstance(result[0]["average"], float)
        assert isinstance(result[0]["age"], int)
    
    def test_mixed_types_detection(self):
 
        test_data = [
            {"id": 1, "scores": [80, 90], "age": 20, "score": [80, 90]},
        ]
        
        result = compute_averages(test_data)
        
        item = result[0]

        assert isinstance(item["honor"], (bool, str))
        assert isinstance(item["modifier"], (int, float, list))


class TestIntegrationScenarios:

    
    def test_function_chain_with_error_handling(self):

        test_students = [
            {
                "id": 1, 
                "scores": [80, 90, 85], 
                "age": 20,
                "score": [80, 90, 85]  
            }
        ]
        

        averages = compute_averages(test_students)
        assert len(averages) == 1
        

        with pytest.raises(TypeError):
            filter_and_sort(averages, 18, 100.0)
    
    def test_data_consistency_across_functions(self):
        test_data = [
            {"id": 1, "scores": [80, 90], "age": 20, "score": [80, 90]},
            {"id": 2, "scores": [85, 95], "age": 22, "score": [85, 95]},
        ]
        
        averages = compute_averages(test_data)
        
        assert averages[0]["id"] == 1
        assert averages[1]["id"] == 2


class TestEdgeCases:

    def test_single_element_handling(self):

        single_data = [
            {"id": 1, "scores": [95], "age": 20, "score": [95]}
        ]
        
        result = compute_averages(single_data)
        assert len(result) == 1
        assert result[0]["average"] == 95.0
    
    def test_extreme_numeric_values(self):

        extreme_data = [
            {"id": 1, "average": 0.0, "age": 0, "adjusted": 0, "final_score": 0},
            {"id": 2, "average": 100.0, "age": 100, "adjusted": 100, "final_score": 100},
        ]
        

        with pytest.raises(TypeError):
            filter_and_sort(extreme_data, 0, 100.0)


class TestCalculationCorrectness:

    def test_average_calculation_with_fixed_key(self):

        test_data = [
            {"id": 1, "scores": [80, 90, 100], "age": 20, "score": [80, 90, 100]},
        ]
        
        result = compute_averages(test_data)
        assert result[0]["average"] == 90.0
    
    def test_adjusted_field_calculation(self):
        test_data = [
            {"id": 1, "scores": [80, 90], "age": 20, "score": [80, 90]},
        ]
        
        result = compute_averages(test_data)
        average = result[0]["average"]
        adjusted = result[0]["adjusted"]
        assert adjusted >= average - 5
        assert adjusted <= average + 5


class TestAdditionalCases:

    def test_none_handling(self):

        test_data = [{"id": 1, "scores": None, "age": 20}]
        result = compute_averages(test_data)
        assert result[0]["average"] is None
    
    def test_string_scores_handling(self):

        test_data = [{"id": 1, "scores": ["80", "90"], "age": 20}]

        with pytest.raises(TypeError):
            compute_averages(test_data)
    
    def test_missing_age_handling(self):

        test_data = [{"id": 1, "scores": [80, 90]}]
        result = compute_averages(test_data)
        assert result[0]["age"] == 0  
    
    def test_large_dataset_performance(self):

        large_data = [{"id": i, "scores": [80, 90], "age": 20} for i in range(1000)]
        result = compute_averages(large_data)
        assert len(result) == 1000


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])