import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/rafsunsheikh/qs_ranking/main/2026_QS_World_University_Rankings.csv"
qs_dataset = pd.read_csv(url)

df = qs_dataset[["2026 QS World University Rankings", "Unnamed: 30"]]

new_df = df.iloc[3:].copy()
new_df.reset_index(drop=True, inplace=True)

new_df["2026 QS World University Rankings"] = pd.to_numeric(new_df["2026 QS World University Rankings"], errors='coerce', downcast='float')
new_df["Unnamed: 30"] = pd.to_numeric(new_df["Unnamed: 30"], errors='coerce', downcast='float')
new_df = new_df.dropna()
new_df.isna().sum()

X = new_df.drop("2026 QS World University Rankings", axis = 1)
y = new_df["2026 QS World University Rankings"]


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
random_forest_reg = RandomForestRegressor(random_state=0)
random_forest_reg.fit(X, y.values)



aca_rep_weight = 0.3
emp_rep_weight = 0.15
fac_stu_ratio_weight = 0.1
cit_per_fac_weight = 0.2
int_fac_ratio_weight = 0.05
int_stu_ratio_weight = 0.05
int_res_net_weight = 0.05
emp_outcome_weight = 0.05
sustainability_weight = 0.05



aca_rep_score = 0.0
emp_rep_score = 0.0
fac_stu_ratio_score = 0.0
cit_per_fac_score = 0.0
int_fac_ratio_score = 0.0
int_stu_ratio_score = 0.0
int_res_net_score = 0.0
emp_outcome_score = 0.0
sustainability_score = 0.0


# Set the page to wide mode to use the full width of the screen
st.set_page_config(layout="wide")




def academic_reputation_section():
  global aca_rep_score
  aca_rep_score_previous = 36.0
  aca_rep_score = st.slider("Academic Reputation Score", 0.0, 100.0, 36.0)
  if aca_rep_score != aca_rep_score_previous:
    international_reputation_weight = 0.85
    domestic_reputation_weight = 0.15
    international_reputation_score = aca_rep_score * international_reputation_weight
    domestic_reputation_score = aca_rep_score * domestic_reputation_weight
    # st.write(f"You have to get {international_reputation_score:.2f}% surveying academician to select this institution internationally within top 30 International university.")
    # st.divider()
    # st.write(f"You have to get {domestic_reputation_score:.2f}% surveying academician to select this institution domestically within top 10 Domestic University.")
    aca_rep_score_previous = aca_rep_score
    # st.divider()
    # st.subheader("How to Achieve?")
    # st.write("1. Elevate the institution's research quality by fostering a culture of innovation and scholarly excellence.")
    # st.write("2. Strengthen academic partnerships by implementing a strategic and collaborative approach.")
    # st.write("3. Enhance the institution's strategic impact on the academic landscape.")
    # st.write("4. Foster a culture of institutional innovativeness, driving meaningful contributions to education and society.")
    # st.write("5. Aspire to rank among the Top 10 Domestic Institutions and the Top 30 International Institutions.")
    # st.write("6. Aim for inclusion among the Top 10 Business Schools, both domestically and internationally")
    # st.divider()



def employer_reputation_section():
  global emp_rep_score
  emp_rep_score_previous = 30.5
  emp_rep_score = st.slider("Employer Reputation Score", 0.0, 100.0, 30.5)
  if emp_rep_score != emp_rep_score_previous:
    international_emp_reputation_weight = 0.5
    domestic_emp_reputation_weight = 0.5
    international_emp_reputation_score = emp_rep_score * international_emp_reputation_weight
    domestic_emp_reputation_score = emp_rep_score * domestic_emp_reputation_weight
    # st.write(f"You have to get {international_emp_reputation_score:.2f}% surveying employer to select this institution internationally within top 30 best International university for producing relevant graduates.")
    # st.divider()
    # st.write(f"You have to get {domestic_emp_reputation_score:.2f}% surveying employer to select this institution internationally within top 10 best Domestic university for producing relevant graduates.")
    emp_rep_score_previous = emp_rep_score
    # st.divider()
    # st.subheader("How to Achieve?")
    # st.write("1. Ensure the successful employment of the majority of undergraduate students upon completion of their first degree.")
    # st.write("2. Foster strong connections with employers to facilitate job placement for our graduates within familiar organizations.")
    # st.write("3. Strive for a global reach by enabling graduates to secure positions at renowned domestic and international organizations.")
    # st.write("4. Cultivate specialized expertise among graduates in specific academic disciplines.")
    # st.write("5. Promote industry-specific specialization among graduates to meet the demands of their respective fields.")
    # st.write("6. Aspire to rank among the Top 10 Domestic Universities for producing relevant graduates.")
    # st.write("7. Aim for inclusion among the Top 30 International Universities known for producing graduates highly sought after by employers.")
    # st.divider()


def faculty_student_ratio_section():
  global fac_stu_ratio_score
  fac_stu_ratio_score_previous = 29.7
  fac_stu_ratio_score = st.slider("Faculty Student Ratio Score", 0.0, 100.0, 29.7)
  if fac_stu_ratio_score != fac_stu_ratio_score_previous:
    estimated_fac_stu_ratio = (107.5-fac_stu_ratio_score)/2.5
    st.write(f"To get the score of {fac_stu_ratio_score}, the institution should have Faculty-Student Ratio of 1:{estimated_fac_stu_ratio:.2f}.")
    fac_stu_ratio_score_previous = fac_stu_ratio_score
    # st.divider()
    # st.subheader("How to Achieve?")
    # st.write("1. Increase the availability of academic staff resources to enhance the student experience, including: Teaching, Supervision, Curriculum development, Pastoral support, ensuring a more enriching experience for students.")
    # st.write("2. Strive to achieve a more favorable ratio between the number of Full-Time Equivalent Faculty and Full-Time Equivalent students, promoting a more personalized and engaging learning environment.")
    # st.divider()




def citation_per_faculty_section():
  global cit_per_fac_score
  cit_per_fac_score = st.slider("Citation Per Faculty Score", 0.0, 100.0, 93.08)



def international_faculty_ratio_section():
  global int_fac_ratio_score
  int_fac_ratio_score_previous = 100.0
  int_fac_ratio_score = st.slider("International Faculty Ratio Score", 0.0, 100.0, 100.0)
  if int_fac_ratio_score != int_fac_ratio_score_previous:
    estimated_int_fac_ratio = (103.64 - int_fac_ratio_score)/1.456
    st.write(f"To get the score of {int_fac_ratio_score}, the institution should have International Faculty Ratio of 1:{estimated_int_fac_ratio:.2f}.")
    int_fac_ratio_score_previous = int_fac_ratio_score
    # st.divider()
    # st.subheader("How to Achieve?")
    # st.write("1. Enhance the proportion of international faculty members relative to the overall staff, fostering a more diverse and globally engaged academic environment.")
    # st.write("2. Ensure that this increase in international faculty contributes positively to research diversity and collaborative efforts, enriching the academic experience.")
    # st.write("3. Strive to increase the number of foreign-national faculty members who contribute to academic teaching, research, or both at the university for a minimum period of at least 3 months, as a proportion of the overall faculty staff.")
    # st.divider()


def international_student_ratio_section():
  global int_stu_ratio_score
  int_stu_ratio_score_previous = 34.83
  int_stu_ratio_score = st.slider("International Student Ratio Score", 0.0, 100.0, 34.83)
  if int_stu_ratio_score != int_stu_ratio_score_previous:
    estimated_int_stu_ratio = (138.0251 - int_stu_ratio_score)/16.43
    st.write(f"To get the score of {int_stu_ratio_score}, the institution should have international Student Ratio of 1:{estimated_int_stu_ratio:.2f}.")
    int_stu_ratio_score_previous = int_stu_ratio_score
    # st.divider()
    # st.subheader("How to Achieve?")
    # st.write("1. Elevate the proportion of international students relative to the overall student body, promoting greater networking opportunities, cultural exchanges, and a more diverse learning environment.")
    # st.write("2. Ensure that this increase in international student enrollment leads to tangible benefits such as enhanced networking, enriched cultural exchanges, and a more diverse and inclusive learning experience.")
    # st.write("3. Strive to expand the total number of undergraduate and postgraduate international students, thereby contributing to a globally engaged and diverse campus community.")
    # st.divider()



def international_research_network_section():
  global int_res_net_score
  int_res_net_score = st.slider("International Research Network Score", 0.0, 100.0, 81.8)

def employment_outcome_section():
  global emp_outcome_score
  emp_outcome_score = st.slider("Employment Outcome Score", 0.0, 100.0, 20.8)

def sustainability_section():
  global sustainability_score
  sustainability_score = st.slider("Sustainablity Score", 0.0, 100.0, 84.8)








def main():

  st.title("QS University Ranking Predictive Dashboard")

  left_column, right_column = st.columns(2)

  with left_column:
    st.subheader("Use the sliders to adjust the scores of each section.")
    academic_reputation_section()
    employer_reputation_section()
    faculty_student_ratio_section()
    citation_per_faculty_section()
    international_faculty_ratio_section()
    international_student_ratio_section()
    international_research_network_section()
    employment_outcome_section()
    sustainability_section()



  with right_column:
    right_left_column, right_right_column = st.columns(2)

    with right_left_column:
      st.write("QS Overall Score")
      st.write("(Higher is better)")

      overall_score_bar_chart_placeholder = st.empty()

      overall_score_placeholder = st.empty()

    with right_right_column:
      st.write("QS Overall Ranking")
      st.write("(Lower is better)")

      overall_rank_bar_chart_placeholder = st.empty()

      overall_rank_placeholder = st.empty()



  overall_aca_rep_score = aca_rep_score * aca_rep_weight

  overall_emp_rep_score = emp_rep_score * emp_rep_weight

  overall_fac_stu_ratio_score = fac_stu_ratio_score * fac_stu_ratio_weight

  overall_cit_per_fac_score = cit_per_fac_score * cit_per_fac_weight

  overall_int_fac_ratio_score = int_fac_ratio_score * int_fac_ratio_weight

  overall_int_stu_ratio_score = int_stu_ratio_score * int_stu_ratio_weight

  overall_int_res_net_score = int_res_net_score * int_res_net_weight

  overall_emp_outcome_score = emp_outcome_score * emp_outcome_weight

  overall_sustainability_score = sustainability_score * sustainability_weight


  # return total_overall_score
  # ok = st.button("Calculate Score")
  # if ok:
  total_overall_score = ( overall_aca_rep_score + overall_emp_rep_score + overall_fac_stu_ratio_score +
                        overall_cit_per_fac_score + overall_int_fac_ratio_score + overall_int_stu_ratio_score +
                          overall_int_res_net_score + overall_emp_outcome_score + overall_sustainability_score)

  pred = np.array([[total_overall_score]])
  rank = random_forest_reg.predict(pred)

  overall_score_placeholder.subheader(f"Score: {total_overall_score:.2f}")
  overall_rank_placeholder.subheader(f"Ranking: {int(rank)}")

  overall_score_bar_chart_placeholder.bar_chart({"a: yet to achieve": [100-total_overall_score],
                      "b: achieved": [total_overall_score]}, use_container_width=False, width=250, height=500, color=["#48ffff", "#ff7648"])


  overall_rank_bar_chart_placeholder.bar_chart({"a: yet to achieve": [548 - int(rank)],
                      "b: achieved": [int(rank)]}, use_container_width=False, width=250, height=500, color=["#abdd87", "#a075c0"])



if __name__ == "__main__":
    main()
