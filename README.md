# RenderCV-Split-YAML

[RenderCV](https://github.com/sinaatalay/rendercv) is a Python engine that takes a YAML file containing content and formatting options, and generate a PDF resume/CV with LaTeX and Jinja. It also generates other viewing format, such as HTML for spellcheckers. 

This scripts I am making here is mainly to allow me to split the different section of the YAML file (cv, design, locale_catalog) into different files. The content sections are also seperated into distint YAML files (e.g education.yaml, experience.yaml) to make it neater to update and manage. 

## Usage

Prerequisites:
- Python 3.12 (any after 3.5 _might_ work)

To use the files here in its entirty, do the following: 
1. Clone this repo and use `setup.bat` sets up a vitural Python environment (in Windows)  
2. Add content and customize the design
3. Run `render.bat` to combine the YAML files and run RenderCV in one command

### 1. Setup

1. Clone this repo
```cmd
git clone https://github.com/GallvinF/RenderCV-Split-YAML.git
```
2. Use `setup.bat` to set up the vitural environment and prepare RenderCV to be used
```cmd
setup.bat YOURNAME [TEMPLATE]
```
`YOURNAME` can be any string and will be used during the RenderCV initialization to create a YAML template, which will not be needed

`TEMPLATE` is optional and decides which template from RenderCV will be downloaded and used. This defaults to `engineeringresumes` if not specified. If you want to use another template, you might have to edit `data_files_yaml/design.yaml` as the settings might be different 

If this batch script executes successfully, you should see this in the folder:
```md 
├─── .venv # python vitural env
│   └─── ...
├─── data_files_yaml
│   └─── sections
├─── engineeringresumes 
├─── markdown
|   └─── ...
├─── combine_yaml.py
├─── README.md
├─── render.bat
├─── requirements.txt
├─── setup.bat
└─── YOURNAME.yaml
```

3. If you do not need the created YOURNAME.yaml created, you can remove it. 

### 2. Content

Next, edit the files in `data_files_yaml/` to customise the resume. For the content of the resume, what you want to edit is `cv.yaml` and the contents in `content`. Below is the default directory layout: 

```md 
├─── sections
│   ├─── certifications.yaml
│   ├─── education.yaml
│   ├─── experience.yaml
│   ├─── order.txt
│   ├─── projects.yaml
│   └─── skills.yaml
├─── cv.yaml
├─── design.yaml
└─── locale_catalog.yaml
```

For more info on how to format, refer to [RenderCV's User Guide](https://docs.rendercv.com/user_guide/structure_of_the_yaml_input_file/) and the examples in the yaml files. In the combining stage, all the data in the sections folder will be added to cv.sections in the combined YAML file. 

However, what you **must** do (aside from adding content) is edit `order.txt` in the sections folder, and order which section comes first with a line break between each listed file. When rendering, the sections are arranged in the order they appear in the YAML file, so this is important. 

(Footnote: For this reason, the python script used to combine all the files does not use PyYAML, as it does not preserve the order and dumps the YAML file in alphabatical order)

### 3. Rendering the Resume 

Simply run `render.bat` and check if there are any errors. This script runs two commands: `combine_yaml.py` to combine the seperate YAML files into one, and the command for RenderCV to generate the resume.

If the python script succeeds, the combined YAML file is created with the name `rendercvResume.yaml`. If the rendering is successful, a new folder `rendercv_output` is created with the generated files. 

## Improvements/TODOs

- Translate `setup.bat` and `render.bat` into Bash scripts if I ever use this on Linux
- Custom template maybe
 - In experience, make the job title first and company second
