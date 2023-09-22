# ML project with Docker
This project helps as a baseline for building a general Machine Learning Project that uses Docker. It can be integrated with the DevContainers extension in VS Code. The project implements:

1) **Docker integration:** Implements a simple devcontainer folder that can be used to build a Docker image using the DevContainers extension from VS Code. It also implements a basic Dockerfile that allows for installing a basic Python version, installing all dependencies in a requirements.txt file in the same folder.
2) **Pre-Commits:** Implements a general pre-commit structure to get instant webhooks using a few libraries that I consider essential: *black*, *isort*, *bandit* and *interrogate*. More can be added using the pre-commit yaml file in the main directory.
3) **.gitignore:** Uses a base .gitignore with things that you generally don't want to publish to a github repository, so that I don't forget to implement them.

# Documentation Template:

## Problem

1) What is the problem we want to solve?
2) Which (strategic) business objective is it linked to?
3) What are the current solutions/workarounds (if any)?
4) Why do we think using machine learning will add value? (Links to similar cases in the industry, papers, research)
5) Which parts of the system will use predictions? Which decisions/actions are possible based on the model’s predictions? Which user journey(s) include using the model, and what impact does it have?
6) What input must the model accept, and what output does it have to produce?

## Metrics

1) Which metric(s) will be used to measure the model’s performance?
2) What is/are the minimal value(s) of metrics for running the model in production?
3) How are the performance measures aligned with the business objectives?
4) What is the performance of the current solution?
5) Is there a way to estimate the value added by machine learning by using historical data?

## Dataset

1) Any selection bias during data collection ? 
2) Are there missing values? If so:
3) Do you know the causes?
4) Do they occur at random? 
5) Are there any known issues with the correctness/accurateness of the data ?
6) Where is data stored? Is it accessible from the infrastructure the DS team is using for training and serving?
7) If data is structured or semi-structured: do you have documentation for each attribute?

## Ethics

1) Could decisions your model makes discriminate against group of users?
2) If so: what should be done
3) regarding the dataset?
4) regarding the feature engineering and modelling?
5) regarding the post-processing of decisions?

## Interpretation

Do we need to interpret the model from any of following points of view?

**Trust:** show that model can make decisions previously made by humans

**Causality:** find which predictors impact the target in which way

**Transferability:** show that the model can predict reasonable results for different inputs, including ones not similar to the training samples

**Informativeness:** if the model is created not for predictions but for measuring the impact of predictors, does it serve this goal?

**Fairness:** show that the model is bias-free

## Legal and Regulatory Requirements

- When training the model, are there any restrictions regarding the preservation of user privacy?
- Any restrictions regarding the use of datasets for the defined purpose?
- Any restrictions regarding the modelling approach?
- Any regulations regarding the development process?

## Reproducibility

- What artifacts of your training do you want to keep or/and historize?
    - code and configurations
    - dataset
    - metrics
    - trained model
    - metadata (date, person who ran the experiment, software/hardware information, etc.)
- How will you achieve this?
- How will you avoid training/serving code skew?

## Testability

- What checks and reports do we need for the dataset before building the model?
    - verifying correctness and completeness of data collection
    - discovering data drift (explanation)
- What checks and reports do we need for the trained model?
    - regarding metrics
    - regarding differences to previous or other versions of the model
- Which grade of automation do we need for each of the defined checks/reports?
    - fully automated incl. decision whether to proceed in the pipeline or stop
    - half automated: generate relevant report, but leave the human to decide if to proceed
    - manually executed and decided by the human

## Model update

- Is any concept drift expected? (explanation)
    - how often should a model be retrained/updated to mitigate it?
    - any other ideas for mitigation, e.g. post-processing
- How quickly must a change in source system be reflected in a new version of the model?

## Production

- What information will you record when making predictions?
- What metrics will you continuously watch in production? What thresholds and alerts will you set based on these metrics ?
- How will you discover a performance degradation in production?
