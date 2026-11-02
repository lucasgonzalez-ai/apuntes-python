import pandas as pd, plotly.graph_objects as go
from plotly.subplots import make_subplots
df=pd.read_csv("airline_bookings_clean.csv")
rate=df.is_cancelled.mean()*100; lost=df[df.is_cancelled].ticket_price.sum()
by=df[df.is_cancelled].groupby("route").ticket_price.sum().sort_values()
mon=df.groupby("month").size()
f=make_subplots(rows=1,cols=2,subplot_titles=("Revenue lost to cancellations, by route (£)","Bookings per month"),horizontal_spacing=.12)
f.add_bar(y=by.index,x=by.values,orientation="h",marker_color=["#e0413a" if r=="LHR-SIN" else "#0a7cf0" for r in by.index],row=1,col=1)
f.add_scatter(x=mon.index,y=mon.values,mode="lines+markers",line=dict(color="#0a7cf0",width=3),row=1,col=2)
f.update_layout(title=dict(text=f"<b>Airline bookings</b>   |   {len(df):,} bookings   |   {rate:.1f}% cancelled   |   £{lost:,.0f} lost",font=dict(size=24)),showlegend=False,template="plotly_white",width=1500,height=720,font=dict(family="Inter, Arial",size=17),margin=dict(l=90,r=40,t=120,b=70))
f.update_annotations(font_size=19); f.update_yaxes(rangemode="tozero",row=1,col=2)
f.write_html("dashboard.html",include_plotlyjs=True,full_html=True)
