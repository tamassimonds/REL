from datetime import datetime
import os
import json

class SolutionLogger:
    def __init__(self, question, solution, max_iterations, marker_model, generator_model):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_dir = os.path.join("logs", "solutions", self.timestamp)
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Log initial metadata
        self.metadata = {
            "question": question,
            "expected_solution": solution,
            "max_iterations": max_iterations,
            "marker_model": marker_model,
            "generator_model": generator_model,
            "timestamp": self.timestamp
        }
        
        with open(os.path.join(self.log_dir, "metadata.json"), "w") as f:
            json.dump(self.metadata, f, indent=2)
    
    def log_initial_attempt(self, working_out, response, temperature):
        with open(os.path.join(self.log_dir, "iteration_0.json"), "w") as f:
            json.dump({
                "working_out": working_out,
                "response": response,
                "temperature": temperature
            }, f, indent=2)
    
    def log_evaluation(self, iteration, is_correct, error_step, error_description, raw_eval):
        with open(os.path.join(self.log_dir, f"evaluation_{iteration}.json"), "w") as f:
            json.dump({
                "is_correct": is_correct,
                "error_step": error_step,
                "error_description": error_description,
                "raw_evaluation": raw_eval
            }, f, indent=2)
    
    def log_iteration(self, iteration, prompt, response, temperature):
        with open(os.path.join(self.log_dir, f"iteration_{iteration}.json"), "w") as f:
            json.dump({
                "prompt": prompt,
                "response": response,
                "temperature": temperature
            }, f, indent=2)
    
    def log_final_results(self, current_response, final_solution, is_correct, iteration, error_description):
        final_results = {
            "final_solution": final_solution,
            "working_out": current_response,
            "is_correct": is_correct,
            "iterations": iteration,
            "error_description": error_description if not is_correct else None,
            "log_directory": self.log_dir
        }
        
        with open(os.path.join(self.log_dir, "final_results.json"), "w") as f:
            json.dump(final_results, f, indent=2)
        
        return final_results 