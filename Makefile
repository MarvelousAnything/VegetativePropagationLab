ENVIRONMENT := VegetativePropagationLab

env:
	conda env create -f $(ENVIRONMENT).yml
activate:
	conda activate $(ENVIRONMENT)
requirements: clean env activate
	conda install --file requirements.txt
export_env:
	conda env export > $(ENVIRONMENT).yml
clean:
	conda deactivate
	conda env remove $(ENVIRONMENT)
