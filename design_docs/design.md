# Design Docs, Overview and Use

[Back to README](README.md)

The purpose of this document is to future-proof this design process in anticipation of Open-Sourcing and the eventuality that the author of this project may have other pressing obligations during the life of the project.

## On This Page

On this page you will find, an explanation of the file structure, and the naming conventions for files and directories. An index of the User Stories, and an index of feature-specific design docs.

A step by step protocol for adding User Stories and the related feature design documentation will be outlined below.

While this design documentation structure may seem un-neccesarily involved and compartmentalized, in light of the possibility that this will later become an open-source project it is the view of this projects author that it will aid in better workflow and understanding of the project as a whole; and facilitate an agile and incremental development process while maintaining the integrity of the project.

## Minimum Viable Product (MVP)

In consideration that this project is intended as a personal use tool without direct commercial impact or remuneration, and accounting for the complexity of all financial analysis; It is the opinion of the Author that the MVP of this project should be defined in light of its most basic utility in providing relevant financial information about a given securities investment opportunity.

The MVP for this project is to include the following:

All features and use-cases not stated here, regardless of their mention in the current user stories should be considered stretch goals for future and continued development; Only to be considered after the stated MVP is fully realized and achieved.

- The ability to enter a company name or ticker symbol and retrieve relevant fundamental and technical data.

- The ability to retrieve and view Fundamental Data regarding a company. fundamental data is to be defined as the Financial statements (Income Statement, Cashflow Statement, Balance Sheet) and navigable links to earnings calls, annual reports, and SEC Filings.

- The ability to retrieve and view Technical data as related to the company's Market price and historical performance.

- The ability to plot any of the provided data points in a 3 dimensional graph, where the 'Z' axis is Time, the 'X' axis an array of the points to plot, and the 'Y' axis the numeric value of those points over time.

## Index of User Stories

[General Use and GUI](design_docs/user_stories/general_use_ui.md)
[Tutorials and Tooltips](design_docs/user_stories/tutorials_education.md)
[3D Visualization and Views](design_docs/user_stories/visualization_3d.md)
[Conditional Analysis](design_docs/user_stories/conditional_analysis.md)
[Strategy Development and Testing](design_docs/user_stories/strategy_dev_test.md)
[Alerts and Push Notifications](design_docs/user_stories/alerts_notifications.md)
[Save Data](design_docs/user_stories/saves.md)
[Quick Analysis](design_docs/user_stories/quick_analysis.md)
[Estimate Taxes](design_docs/user_stories/tax_estimate.md)
[Memory and Storage Management](design_docs/user_stories/memory_management.md)

## Index Of Feature Design Docs

[Main Window](design_docs/feature_docs/main_window/main_win.md)

### File Structure and Naming Conventions

The file structure for design documentation should be maintained as shown below in the `design_docs` directory of the project. User stories are to be contained in the `user_stories` sub-directory and file names should be descriptive of the goal outlined by the story within. The header of `<user_story>.md` files should be a descriptive long-form of the fileName.

**Example:**

```Markdown
    1 // fileName: general_use_ui.md
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

```Markdown
    1 // pwd: "./design_docs/feature_docs/main_window/"
    2 // fileName: main_win_design.md
    3 
    4 # Designing the Main Application Window
    5 
    6 [Back to README](README.md)
    7 [Back to design.md](design.md)
    8 [User_Story General Use and UI](general_use_ui.md)
    9 
   10 The main window should default to width:300px and hieght: 400px....
   11 
   12...
   13
   14 // EOF

```

Each feature directory should also contain supporting visual models as `.png` files, including but not limited to: whiteboards, wire-frames, domain models, and wrrc.

**Example:**

```Markdown
    1 // tree of design_docs directory
    2
    3 design_docs
    4   \__user_stories
    5   \__feature_docs
    6       \__main_window
    7           \__main_win.md
    8           \__main_win_wiref.png
    9           \__main_win_model.png
   10           \__main_win_class_rel.png
   11
   12       \__menu_options
   13           \__menu_opt.md
   14           \__menu_opt_model.png
   15
   16  

```

The `pkg_lib.md` file is to contain a list of all external libraries, packages, and API's with a brief description of the resource, it's purpose within the application and a link directly to the Documentation for that resource. If a new feature requires a resource not previously included, it should be noted in the design doc for that feature, the resource should be added to the `pkg_lib.md` and a link to that entry should be included in the design document.

**Example:**

```Markdown
    1 // pwd: "/design_docs/"
    2 // fileName: pkg_lib.md
    3 
    4 # External Resources, Packages, Libraries
    5
    6 **_[Tkinter](https://tkdocs.com/)
    7
    8 The Tkinter module is used as the base framework for creating the GUI 9 for this application and managing user interface. Click the module
   10 name above to be taken to the Tkinter Documentation homepage, or here: 11 [Tkinter Tutorial](https://tkdocs.com/tutorial/index.html) to be 
   12 taken directly to the tutorial and reference pages. 
   13
   14...
   15
   16 // EOF 

```

### Updating the Design Docs

When a New Feature or Feature set is to be added, the design documentation should be submitted with a pull request prior to any work on the implementation. All work on design documentation should be done on the `<user_stories>` branch or on a branch named for the proposed feature. Design and Implementation branches should be differentiated by including `_design` or `_imp` after the featureName. FeatureName for branches should match the feature name for the feature's Markdown file. All branchNames with the exception of the `<user_stories>` branch, should be trailed with the developer's initials in CAPS. `<general_use_ui_design_MC>` or `<general_use_ui_imp_MC>`

**Example:**

```Markdown
    1 // action/proposal: a new user story highlighting new features to be added.
    2 branch: <user_stories>
    3 
    4 // action/proposal: update design_docs with new feature
    5 branch: <featureName_design_devInitials>
    6 
    7 // action/proposal: implementation of the design
    8 branch: <featureName_imp_devInitials>
```

---

1. On `<user_stories>` branch add relevant user story. Submit Pull Request.

2. On branch with `_design` (see above regarding branch naming conventions), add a feature sub-directory under `feature_docs`

3. Add the design markdown file as described above and any supporting visual assets

4. If feature requires the use of a package, library, or API not previously used, update `pkg_lib.md` as described above.

5. Back-link the feature markdown file to `design.md` index section

6. Submit pull request.

---

### Feature Implementation

For work on implementation of a feature, work on an appropriately named branch, (see above) and be sure to only work on features with approved design documentation that has been merged to `<main>` branch.

Submit all pull requests to the `<testing>` branch.

If you are working on an existing feature, either improving functionality or optimizing/re-factoring existing code, please do all work on a branch with the `_refactor` designator in place of `_design` or `_imp` as described above.

Pull requests tagged with `_refactor` should be submitted to the `<optimization>` branch with a relevant comment explaining what the benefit of the proposed refactor is.
