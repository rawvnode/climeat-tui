## Climeat (Genre: Fiction)

To deter consumption of meat and effectively reduce greenhouse gas emissions.

## Team

<details>
<summary>Ani</summary>

**Ani Darejan** -> Role: Product Owner (Storyteller)
>“I hope that in this year to come, you make mistakes. Because if you are making mistakes...you're Doing Something.”
― Neil Gaiman

</details>

<details>
<summary>Natasha</summary>

**Natasha Ninoslav** -> Role: Developer (Creative)
>“Software engineering is programming integrated over time.”
― Titus Winters

Toolbox : Python, Jupyter, FastAPI, Data engineering, PostgreSQL

</details>

<details>
<summary>Dipak</summary>

**Dipak Vera** -> Role: SRE (Realist)
>“All models are wrong, but some are useful”
― George Box

Toolbox : Kubernetes, GitOps, Helm, Loki, Tempo, k6, Postgres performance utilities

</details>



*Names generated using [Behind the Name](https://www.behindthename.com/random/)* 

## Pitch

<details>
<summary>Pitch - Derive insights from CDP dataset</summary>

**__By Ani Darejan__**

Our team of climate sustainability experts suggested that we look into the CDP dataset that scores companies and cities based on their journey through disclosure towards environmental leadership.

**Example case**

![KPIs for Food Waste, Insecurity & Overconsumption](https://www.kaggle.com/abdulwahabkabani/kpis-for-food-waste-insecurity-overconsumption/notebook) - Abdulwahab Kahani describes the problem of food waste and overconsumption very well. He refers to food overconsumption as a state in which food intake exceeds individual food requirements, providing an excess of nutrients and energy and meat overconsumption as a case where a person eats more than their recommended daily intake.

**Looking for a 1-weeker**

There are numerous opportunities to derive insights from the above solution, but given the timeline around the launch of the awareness campaign, I'd like to focus our efforts on creating a dashboard that provides insight into meat overconsumption. For this short iteration, we could explore the city disclosures based on public responses to have an impact on the campaign given our target audience.

**Metrics**

I think the metrics,annual meat consumption per capita and city-wide amount of meat consumed that is above the limit, should effectively raise awareness of meat overconsumption.

</details>

## Team Interaction

<details>
<summary>Team interaction</summary>

## Day 1

```markdown
[09:00] *** <Ani> Natasha, can you review the Kaggle notebook listed in my pitch specifically section 4?
[09:01] *** <Natasha> 👍 
[11:00] *** <Natasha> Ani, im able to get the notebook working on my local...moving onto data wrangling
[11:15] *** <Ani> 👍 
```

## Day 2

```markdown
[10:58] *** <Natasha> Ani, i was able to import the csv files into 2 tables - cities and city_responses
[10:58] *** <Natasha> i created an utility table to capture the latest city population datapoint
[11:00] *** <Natasha> all 3 tables are related using the city account number which is unique to cities and city population tables
[11:00] *** <Natasha> Ani, check out the /meatcity endpoint
[11:00] *** <Natasha> the solution to the dataset heavily employs Pandas dataframes for analysis
[11:01] *** <Natasha> next steps, look into pivoting data from rows to columns in sql
[13:30] *** <Ani> 👍 
```

## Day 3

```markdown
[11:00] *** <Natasha> Ani, the /meatcities endpoint is available to test. lmk what you think
[11:45] *** Joins: Dipak
[11:45] *** <Dipak> Natasha, did you put the endpoints through the Trials of Chaos 💪
[11:45] *** <Dipak> i encoded a few test rules based on the feedback i received from Ani on user volume.
[13:30] *** <Natasha> 🙏 can't wait to play
[15:00] *** <ToC Bot> City Level 1 ✅ 
[15:00] *** <ToC Bot> Meat Cities Level 1 ❌
```

## Day 4

```markdown
[15:30] *** <Dipak> Natasha, i added some recommendation after reviewing your comment
[16:00] *** <Natasha> 👍 
```

## Day 5

```markdown
[10:00] *** <ToC Bot> Meat Cities Level 1 ✅ 
[09:01] *** <Natasha> Dipak, thanks for the advice...i will continue to explore other options to improve the performance further
[11:00] *** <Natasha> Ani, release code?
[11:00] *** <Ani> 🤗 
[15:00] *** <Deploy Bot> 🚀 
```