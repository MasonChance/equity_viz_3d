# Tooltip and Information, Display Frame

- [Back to README](../../../README.md)
- [Back to Design Docs](../../design.md)

Main window should have a section dedicated to displaying information about any element of the the application or the application readout the cursor is hovered over.

## User Stories

- [Tutorials and Education](../../user_stories/tutorials_education.md)
- [General Use and UI](../../user_stories/general_use_ui.md)

## Required Packages and Resources

For more details on a given resource, see [Packages And Libraries](../../pkg_lib.md). This feature should only require the python built-ins: JSON, and sys.

### Overview of Design Approach

There should be a default text welcoming the user and describing the general use and navigation of the application as well as where to find more detailed information as the application develops.

Tooltips regarding the buttons and readout areas should pull their information from either a JSON file (to function much like a settings.JSON) or from a Python Dictionary. Keys or Properties should be descriptive of the button/section/readout, and where possible be limited to one word without the need for underscores.

Tooltips regarding complex features or elements, should contain external links (utilizing the system's default browser) to further resources and information.

**Example:**

```Markdown

    // tooltip regarding label: "EPS"
    // when user hovers over above label tootip section should read:

    "EPS is an acronym for 'Earnings Per Share', this is used as a general measure of how much the company earned for a given period for every outstanding share of stock issued by the company. For more detailed information regarding EPS and its use in a company's valuation see: https//:www.investopia.com "

    // NOTE: link in example for demonstration purposes only, the actual link used in a tooltip with external resources should be chosen for it's clarity and free availability.

```

Implementation of the tooltip feature will be heavily entwined with the implementation of each individual feature/ui_window and thus each feature should be implemented as an element of a class or class method where possible, and those classes should have a "tooltip" property with a value correlated to a key of the tooltip.JSON object.

For Ease of Develpment and adding/removing tooltips, a tooltip class should be implemented as a private class with private methods related to the creation and deletion of tooltips from the JSON object. This should allow developers to run python interpreter in the command line within the relevant directory and update the tooltip.JSON with a function, rather than manually editing the file. If only the content of a tooltip needs editing, ie: external links, display text, etc. devs should edit this in the file directly to ensure consistency and precision. For useage docs See: [dev_utilities](../../../_utilities/_util.md)

**Class Models and Whiteboards:**

![tooltip_utility_class_model](tooltip_class_model.png)

![tooltip_utility_whiteboard](tooltip_wboard.png)

NOTE: tooltip.JSON should be located at the root of the project. files defining the tooltip class and it's methods should be located in the private `_utilities` directory.
