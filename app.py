import pandas as pd
import plotly.express as px

from dash import (
    Dash,
    dcc,
    html,
    dash_table,
    Input,
    Output,
    State
)

import dash_bootstrap_components as dbc


# =========================================================
# 1. LOAD DATA
# =========================================================

df = pd.read_csv("titanic.csv")


# =========================================================
# 2. DATA CLEANING
# =========================================================

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")


MAX_AGE = int(df["Age"].max())
MAX_FARE = int(df["Fare"].max())


# =========================================================
# 3. APP
# =========================================================

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP
    ]
)

app.title = "Titanic Analytics Dashboard"


# =========================================================
# 4. KPI CARD
# =========================================================

def kpi_card(title, value_id):

    return dbc.Card(

        dbc.CardBody([

            html.P(
                title,
                className="mb-1"
            ),

            html.H3(
                id=value_id,
                className="fw-bold mb-0"
            )

        ]),

        id=f"{value_id}-card",

        className="kpi-card shadow-sm"

    )


# =========================================================
# 5. SIDEBAR
# =========================================================

sidebar = dbc.Card(

    dbc.CardBody([

        html.H2(
            "🚢 Titanic",
            className="text-center"
        ),

        html.P(
            "Analytics Dashboard",
            id="sidebar-subtitle",
            className="text-center"
        ),

        html.Hr(),


        # =================================================
        # THEME
        # =================================================

        html.Label(
            "🎨 Theme",
            className="fw-bold"
        ),

        dcc.RadioItems(

            id="theme-selector",

            options=[

                {
                    "label": " ☀️ Light",
                    "value": "light"
                },

                {
                    "label": " 🌙 Dark",
                    "value": "dark"
                }

            ],

            value="light",

            inline=True,

            className="mb-3"

        ),


        # =================================================
        # GENDER
        # =================================================

        html.Label(
            "👤 Gender",
            className="fw-bold"
        ),

        dcc.Dropdown(

            id="gender-filter",

            options=[

                {
                    "label": "All",
                    "value": "All"
                },

                {
                    "label": "Male",
                    "value": "male"
                },

                {
                    "label": "Female",
                    "value": "female"
                }

            ],

            value="All",

            clearable=False

        ),

        html.Br(),


        # =================================================
        # CLASS
        # =================================================

        html.Label(
            "🎫 Passenger Class",
            className="fw-bold"
        ),

        dcc.Dropdown(

            id="class-filter",

            options=[

                {
                    "label": "All Classes",
                    "value": "All"
                },

                {
                    "label": "1st Class",
                    "value": 1
                },

                {
                    "label": "2nd Class",
                    "value": 2
                },

                {
                    "label": "3rd Class",
                    "value": 3
                }

            ],

            value="All",

            clearable=False

        ),

        html.Br(),


        # =================================================
        # EMBARKED
        # =================================================

        html.Label(
            "⚓ Embarked",
            className="fw-bold"
        ),

        dcc.Dropdown(

            id="embarked-filter",

            options=[

                {
                    "label": "All",
                    "value": "All"
                },

                {
                    "label": "Southampton",
                    "value": "S"
                },

                {
                    "label": "Cherbourg",
                    "value": "C"
                },

                {
                    "label": "Queenstown",
                    "value": "Q"
                }

            ],

            value="All",

            clearable=False

        ),

        html.Br(),


        # =================================================
        # SURVIVAL
        # =================================================

        html.Label(
            "❤️ Survival",
            className="fw-bold"
        ),

        dcc.Dropdown(

            id="survival-filter",

            options=[

                {
                    "label": "All",
                    "value": "All"
                },

                {
                    "label": "Survived",
                    "value": 1
                },

                {
                    "label": "Died",
                    "value": 0
                }

            ],

            value="All",

            clearable=False

        ),

        html.Br(),


        # =================================================
        # AGE
        # =================================================

        html.Label(
            "🎂 Age Range",
            className="fw-bold"
        ),

        dcc.RangeSlider(

            id="age-slider",

            min=0,

            max=MAX_AGE,

            value=[
                0,
                MAX_AGE
            ],

            step=1,

            tooltip={
                "placement": "bottom",
                "always_visible": True
            }

        ),

        html.Br(),


        # =================================================
        # FARE
        # =================================================

        html.Label(
            "💰 Fare Range",
            className="fw-bold"
        ),

        dcc.RangeSlider(

            id="fare-slider",

            min=0,

            max=MAX_FARE,

            value=[
                0,
                MAX_FARE
            ],

            step=1,

            tooltip={
                "placement": "bottom",
                "always_visible": True
            }

        ),

        html.Br(),


        # =================================================
        # RESET
        # =================================================

        dbc.Button(

            "🔄 Reset All Filters",

            id="reset-button",

            color="secondary",

            className="w-100 mb-2"

        ),


        # =================================================
        # DOWNLOAD
        # =================================================

        dbc.Button(

            "📥 Download CSV",

            id="download-button",

            color="primary",

            className="w-100"

        ),

        dcc.Download(
            id="download-data"
        )

    ]),

    id="sidebar",

    className="shadow-sm"

)


# =========================================================
# 6. MAIN CONTENT
# =========================================================

main_content = html.Div(

    [

        html.H1(
            "Titanic Passenger Analytics",
            id="main-title",
            className="fw-bold"
        ),

        html.P(
            "Interactive Data Science Dashboard",
            id="main-subtitle"
        ),

        html.Hr(),


        # =================================================
        # KPI CARDS
        # =================================================

        dbc.Row([

            dbc.Col(
                kpi_card(
                    "Total Passengers",
                    "total-passengers"
                ),
                xs=12,
                sm=6,
                lg=3,
                className="mb-3"
            ),

            dbc.Col(
                kpi_card(
                    "Survived",
                    "total-survived"
                ),
                xs=12,
                sm=6,
                lg=3,
                className="mb-3"
            ),

            dbc.Col(
                kpi_card(
                    "Deaths",
                    "total-deaths"
                ),
                xs=12,
                sm=6,
                lg=3,
                className="mb-3"
            ),

            dbc.Col(
                kpi_card(
                    "Survival Rate",
                    "survival-rate"
                ),
                xs=12,
                sm=6,
                lg=3,
                className="mb-3"
            )

        ]),

        html.Br(),


        # =================================================
        # SURVIVAL ANALYSIS
        # =================================================

        html.H2(
            "📊 Survival Analysis",
            id="survival-heading"
        ),

        dbc.Row([

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="survival-gender-chart"
                    ),

                    id="survival-gender-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            ),

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="survival-class-chart"
                    ),

                    id="survival-class-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            )

        ]),


        dbc.Row([

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="survival-age-chart"
                    ),

                    id="survival-age-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            ),

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="survival-embarked-chart"
                    ),

                    id="survival-embarked-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            )

        ]),


        # =================================================
        # EXPLORATORY ANALYSIS
        # =================================================

        html.H2(
            "📈 Exploratory Analysis",
            id="explore-heading"
        ),

        dbc.Row([

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="survival-chart"
                    ),

                    id="survival-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            ),

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="gender-chart"
                    ),

                    id="gender-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            )

        ]),


        dbc.Row([

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="age-chart"
                    ),

                    id="age-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            ),

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="fare-chart"
                    ),

                    id="fare-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            )

        ]),


        dbc.Row([

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="scatter-chart"
                    ),

                    id="scatter-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            ),

            dbc.Col(

                dbc.Card(

                    dcc.Graph(
                        id="heatmap-chart"
                    ),

                    id="heatmap-card"

                ),

                xs=12,
                lg=6,
                className="mb-4"

            )

        ]),


        # =================================================
        # TABLE
        # =================================================

        html.H2(
            "📋 Passenger Data",
            id="table-heading"
        ),

        html.P(
            "Search, filter and sort passenger records.",
            id="table-description"
        ),

        dbc.Input(

            id="global-search",

            placeholder=(
                "🔍 Search passenger name, "
                "ticket, gender, cabin..."
            ),

            className="mb-3"

        ),


        dash_table.DataTable(

            id="data-table",

            page_current=0,

            page_size=10,

            page_action="native",

            sort_action="native",

            sort_mode="multi",

            filter_action="native",

            style_table={
                "overflowX": "auto"
            },

            style_cell={

                "textAlign": "left",

                "padding": "8px",

                "minWidth": "100px",

                "whiteSpace": "normal"

            }

        )

    ],

    id="main-content",

    className="p-3"

)


# =========================================================
# 7. LAYOUT
# =========================================================

app.layout = html.Div(

    [

        dbc.Container(

            [

                dbc.Row([

                    dbc.Col(

                        sidebar,

                        xs=12,
                        lg=3,

                        className="mb-4"

                    ),

                    dbc.Col(

                        main_content,

                        xs=12,
                        lg=9

                    )

                ])

            ],

            fluid=True,

            className="p-3"

        )

    ],

    id="app-container",

    className="light-mode"

)


# =========================================================
# 8. RESET FILTERS
# =========================================================

@app.callback(

    [

        Output(
            "gender-filter",
            "value"
        ),

        Output(
            "class-filter",
            "value"
        ),

        Output(
            "embarked-filter",
            "value"
        ),

        Output(
            "survival-filter",
            "value"
        ),

        Output(
            "age-slider",
            "value"
        ),

        Output(
            "fare-slider",
            "value"
        ),

        Output(
            "global-search",
            "value"
        )

    ],

    Input(
        "reset-button",
        "n_clicks"
    ),

    prevent_initial_call=True

)

def reset_filters(n_clicks):

    return (

        "All",

        "All",

        "All",

        "All",

        [0, MAX_AGE],

        [0, MAX_FARE],

        ""

    )


# =========================================================
# 9. DARK / LIGHT MODE
# =========================================================

@app.callback(

    [

        Output(
            "app-container",
            "className"
        ),

        Output(
            "sidebar",
            "className"
        ),

        Output(
            "main-title",
            "className"
        ),

        Output(
            "main-subtitle",
            "className"
        ),

        Output(
            "sidebar-subtitle",
            "className"
        ),

        Output(
            "survival-heading",
            "className"
        ),

        Output(
            "explore-heading",
            "className"
        ),

        Output(
            "table-heading",
            "className"
        ),

        Output(
            "table-description",
            "className"
        ),

        Output(
            "data-table",
            "style_header"
        ),

        Output(
            "data-table",
            "style_data"
        ),

        Output(
            "data-table",
            "style_cell"
        )

    ],

    Input(
        "theme-selector",
        "value"
    )

)

def change_theme(theme):


    # =====================================================
    # DARK
    # =====================================================

    if theme == "dark":

        return (

            "dark-mode",

            "shadow-sm dark-card",

            "fw-bold dark-text",

            "dark-muted",

            "dark-muted text-center",

            "dark-text",

            "dark-text",

            "dark-text",

            "dark-muted",

            {
                "backgroundColor": "#2d2d2d",
                "color": "#ffffff",
                "fontWeight": "bold",
                "border": "1px solid #555"
            },

            {
                "backgroundColor": "#1e1e1e",
                "color": "#ffffff",
                "border": "1px solid #444"
            },

            {
                "textAlign": "left",
                "padding": "8px",
                "minWidth": "100px",
                "whiteSpace": "normal",
                "backgroundColor": "#1e1e1e",
                "color": "#ffffff",
                "border": "1px solid #444"
            }

        )


    # =====================================================
    # LIGHT
    # =====================================================

    return (

        "light-mode",

        "shadow-sm",

        "fw-bold",

        "",

        "text-center",

        "",

        "",

        "",

        "",

        {
            "backgroundColor": "#e9ecef",
            "color": "#212529",
            "fontWeight": "bold",
            "border": "1px solid #dee2e6"
        },

        {
            "backgroundColor": "#ffffff",
            "color": "#212529",
            "border": "1px solid #dee2e6"
        },

        {
            "textAlign": "left",
            "padding": "8px",
            "minWidth": "100px",
            "whiteSpace": "normal",
            "backgroundColor": "#ffffff",
            "color": "#212529",
            "border": "1px solid #dee2e6"
        }

    )


# =========================================================
# 10. DASHBOARD CALLBACK
# =========================================================

@app.callback(

    [

        Output(
            "total-passengers",
            "children"
        ),

        Output(
            "total-survived",
            "children"
        ),

        Output(
            "total-deaths",
            "children"
        ),

        Output(
            "survival-rate",
            "children"
        ),

        Output(
            "survival-gender-chart",
            "figure"
        ),

        Output(
            "survival-class-chart",
            "figure"
        ),

        Output(
            "survival-age-chart",
            "figure"
        ),

        Output(
            "survival-embarked-chart",
            "figure"
        ),

        Output(
            "survival-chart",
            "figure"
        ),

        Output(
            "gender-chart",
            "figure"
        ),

        Output(
            "age-chart",
            "figure"
        ),

        Output(
            "fare-chart",
            "figure"
        ),

        Output(
            "scatter-chart",
            "figure"
        ),

        Output(
            "heatmap-chart",
            "figure"
        ),

        Output(
            "data-table",
            "data"
        ),

        Output(
            "data-table",
            "columns"
        )

    ],

    [

        Input(
            "gender-filter",
            "value"
        ),

        Input(
            "class-filter",
            "value"
        ),

        Input(
            "embarked-filter",
            "value"
        ),

        Input(
            "survival-filter",
            "value"
        ),

        Input(
            "age-slider",
            "value"
        ),

        Input(
            "fare-slider",
            "value"
        ),

        Input(
            "global-search",
            "value"
        ),

        Input(
            "theme-selector",
            "value"
        )

    ]

)

def update_dashboard(

    gender,
    passenger_class,
    embarked,
    survival,
    age_range,
    fare_range,
    search_text,
    theme

):

    filtered = df.copy()


    # =====================================================
    # FILTER
    # =====================================================

    if gender != "All":

        filtered = filtered[
            filtered["Sex"] == gender
        ]


    if passenger_class != "All":

        filtered = filtered[
            filtered["Pclass"] == passenger_class
        ]


    if embarked != "All":

        filtered = filtered[
            filtered["Embarked"] == embarked
        ]


    if survival != "All":

        filtered = filtered[
            filtered["Survived"] == survival
        ]


    filtered = filtered[

        (filtered["Age"] >= age_range[0])

        &

        (filtered["Age"] <= age_range[1])

    ]


    filtered = filtered[

        (filtered["Fare"] >= fare_range[0])

        &

        (filtered["Fare"] <= fare_range[1])

    ]


    # =====================================================
    # SEARCH
    # =====================================================

    if search_text:

        search_text = str(
            search_text
        ).lower()

        mask = (

            filtered
            .astype(str)
            .apply(

                lambda row:
                row.str.lower()
                .str.contains(
                    search_text,
                    na=False
                )

            )
            .any(axis=1)

        )

        filtered = filtered[mask]


    # =====================================================
    # KPI
    # =====================================================

    total = len(filtered)

    survived_count = int(
        filtered["Survived"].sum()
    )

    deaths = total - survived_count

    survival_rate = (

        survived_count / total * 100

        if total > 0

        else 0

    )


    # =====================================================
    # PLOTLY THEME
    # =====================================================

    template = (
        "plotly_dark"
        if theme == "dark"
        else "plotly_white"
    )


    # =====================================================
    # SURVIVAL BY GENDER
    # =====================================================

    gender_survival = (

        filtered
        .groupby("Sex")["Survived"]
        .mean()
        .reset_index()

    )

    gender_survival["Survival Rate"] = (
        gender_survival["Survived"] * 100
    )


    fig_survival_gender = px.bar(

        gender_survival,

        x="Sex",

        y="Survival Rate",

        text="Survival Rate",

        title="❤️ Survival Rate by Gender",

        range_y=[0, 100],

        template=template

    )

    fig_survival_gender.update_traces(
        texttemplate="%{text:.1f}%"
    )


    # =====================================================
    # SURVIVAL BY CLASS
    # =====================================================

    class_survival = (

        filtered
        .groupby("Pclass")["Survived"]
        .mean()
        .reset_index()

    )

    class_survival["Survival Rate"] = (
        class_survival["Survived"] * 100
    )


    fig_survival_class = px.bar(

        class_survival,

        x="Pclass",

        y="Survival Rate",

        text="Survival Rate",

        title="🎫 Survival Rate by Passenger Class",

        range_y=[0, 100],

        template=template

    )

    fig_survival_class.update_traces(
        texttemplate="%{text:.1f}%"
    )


    # =====================================================
    # AGE GROUP
    # =====================================================

    temp = filtered.copy()

    temp["AgeGroup"] = pd.cut(

        temp["Age"],

        bins=[
            0,
            10,
            20,
            30,
            40,
            50,
            60,
            70,
            100
        ],

        labels=[
            "0-10",
            "11-20",
            "21-30",
            "31-40",
            "41-50",
            "51-60",
            "61-70",
            "71+"
        ]

    )


    age_survival = (

        temp
        .groupby(
            "AgeGroup",
            observed=False
        )["Survived"]
        .mean()
        .reset_index()

    )

    age_survival["Survival Rate"] = (
        age_survival["Survived"] * 100
    )


    fig_survival_age = px.line(

        age_survival,

        x="AgeGroup",

        y="Survival Rate",

        markers=True,

        title="🎂 Survival Rate by Age Group",

        range_y=[0, 100],

        template=template

    )


    # =====================================================
    # EMBARKED
    # =====================================================

    embarked_survival = (

        filtered
        .groupby("Embarked")["Survived"]
        .mean()
        .reset_index()

    )

    embarked_survival["Survival Rate"] = (
        embarked_survival["Survived"] * 100
    )


    fig_survival_embarked = px.bar(

        embarked_survival,

        x="Embarked",

        y="Survival Rate",

        text="Survival Rate",

        title="⚓ Survival Rate by Embarked Port",

        range_y=[0, 100],

        template=template

    )

    fig_survival_embarked.update_traces(
        texttemplate="%{text:.1f}%"
    )


    # =====================================================
    # SURVIVAL COUNT
    # =====================================================

    survival_data = (

        filtered
        .groupby("Survived")
        .size()
        .reset_index(name="Count")

    )

    survival_data["Status"] = (
        survival_data["Survived"]
        .map({
            0: "Died",
            1: "Survived"
        })
    )


    fig_survival = px.bar(

        survival_data,

        x="Status",

        y="Count",

        text="Count",

        color="Status",

        title="Survived vs Died",

        template=template

    )


    # =====================================================
    # GENDER
    # =====================================================

    gender_data = (

        filtered
        .groupby("Sex")
        .size()
        .reset_index(name="Count")

    )


    fig_gender = px.pie(

        gender_data,

        names="Sex",

        values="Count",

        hole=0.45,

        title="Passengers by Gender",

        template=template

    )


    # =====================================================
    # AGE
    # =====================================================

    fig_age = px.histogram(

        filtered,

        x="Age",

        color="Sex",

        nbins=30,

        marginal="box",

        title="Age Distribution",

        template=template

    )


    # =====================================================
    # FARE
    # =====================================================

    fig_fare = px.box(

        filtered,

        x="Pclass",

        y="Fare",

        color="Sex",

        points="all",

        title="Fare Distribution by Class",

        template=template

    )


    # =====================================================
    # SCATTER
    # =====================================================

    fig_scatter = px.scatter(

        filtered,

        x="Age",

        y="Fare",

        color="Survived",

        size="Pclass",

        hover_data=[
            "Name",
            "Sex",
            "Pclass",
            "Ticket"
        ],

        title="Age vs Fare",

        template=template

    )


    # =====================================================
    # HEATMAP
    # =====================================================

    numeric_columns = [

        "Survived",
        "Pclass",
        "Age",
        "SibSp",
        "Parch",
        "Fare"

    ]


    if len(filtered) > 1:

        correlation = (
            filtered[numeric_columns].corr()
        )

    else:

        correlation = pd.DataFrame(
            columns=numeric_columns
        )


    fig_heatmap = px.imshow(

        correlation,

        text_auto=True,

        title="Correlation Heatmap",

        aspect="auto",

        template=template

    )


    # =====================================================
    # TABLE
    # =====================================================

    table_data = filtered.to_dict(
        "records"
    )

    table_columns = [

        {
            "name": column,
            "id": column
        }

        for column in filtered.columns

    ]


    return (

        f"{total:,}",

        f"{survived_count:,}",

        f"{deaths:,}",

        f"{survival_rate:.2f}%",

        fig_survival_gender,

        fig_survival_class,

        fig_survival_age,

        fig_survival_embarked,

        fig_survival,

        fig_gender,

        fig_age,

        fig_fare,

        fig_scatter,

        fig_heatmap,

        table_data,

        table_columns

    )


# =========================================================
# 11. DOWNLOAD CSV
# =========================================================

@app.callback(

    Output(
        "download-data",
        "data"
    ),

    Input(
        "download-button",
        "n_clicks"
    ),

    [

        State(
            "gender-filter",
            "value"
        ),

        State(
            "class-filter",
            "value"
        ),

        State(
            "embarked-filter",
            "value"
        ),

        State(
            "survival-filter",
            "value"
        ),

        State(
            "age-slider",
            "value"
        ),

        State(
            "fare-slider",
            "value"
        ),

        State(
            "global-search",
            "value"
        )

    ],

    prevent_initial_call=True

)

def download_filtered_data(

    n_clicks,
    gender,
    passenger_class,
    embarked,
    survival,
    age_range,
    fare_range,
    search_text

):

    filtered = df.copy()


    if gender != "All":

        filtered = filtered[
            filtered["Sex"] == gender
        ]


    if passenger_class != "All":

        filtered = filtered[
            filtered["Pclass"] == passenger_class
        ]


    if embarked != "All":

        filtered = filtered[
            filtered["Embarked"] == embarked
        ]


    if survival != "All":

        filtered = filtered[
            filtered["Survived"] == survival
        ]


    filtered = filtered[

        (filtered["Age"] >= age_range[0])

        &

        (filtered["Age"] <= age_range[1])

    ]


    filtered = filtered[

        (filtered["Fare"] >= fare_range[0])

        &

        (filtered["Fare"] <= fare_range[1])

    ]


    if search_text:

        search_text = str(
            search_text
        ).lower()

        mask = (

            filtered
            .astype(str)
            .apply(

                lambda row:
                row.str.lower()
                .str.contains(
                    search_text,
                    na=False
                )

            )
            .any(axis=1)

        )

        filtered = filtered[mask]


    return dcc.send_data_frame(

        filtered.to_csv,

        "titanic_filtered.csv",

        index=False

    )


# =========================================================
# 12. RUN
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)