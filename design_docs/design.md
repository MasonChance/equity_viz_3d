# Design Docs, Overview and Use

[Back to README](README.md)

The purpose of this document is to future-proof this design process in anticipation of Open-Sourcing and the eventuality that the creator of this project may have other pressing obligations during the life of the project.

## On This Page

On this page you will find, an explanation of the file structure, and the naming conventions for files and directories. An index of the User Stories, and an index of feature-specific design docs.

A step by step protocol for adding User Stories and the related feature design documentation will be outlined below.

### File Structure and Naming Conventions

The file structure for design documentation should be maintained as shown below in the `design_docs` directory of the project. User stories are to be contained in the `user_stories` sub-directory and file names should be descriptive of the goal outlined by the story within. The header of `<user_story>.md` files should be a descriptive long-form of the fileName.

**Example:**

``` 1 // fileName: general_use_ui.md
    2
    3 # General Use and the GUI
    4
    5 As a user I would like...
    6
    7...
    8
    9 // EOF
```

Each feature should have its own sub-directory in the `design_docs/feature_docs/` directory. Feature directories should follow the file-name pattern of the user stories by being as descriptive as possible. The markdown file describing the overall design and problem domain of that feature should be named identically to it's parent directory, or sensibly abbreviated from it. The top of a feature markdown file should contain a link to both this file, `design.md` and the root `README.md` file, as well as any related user stories the feature is intended to address.

**Example:**

``` 1 // pwd: "./design_docs/feature_docs/main_window/"
    2 // fileName: main_win_design.md
    3 
    4 # Designing the Main Application Window
    5 
    6 [Back to README](README.md)

```