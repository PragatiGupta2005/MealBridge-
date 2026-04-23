import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import hashlib, json, csv, calendar, os
from datetime import datetime, timedelta
import math

# ══════════════════════════════════════════════════════════════
#  THEMES  (Feature 14)
# ══════════════════════════════════════════════════════════════
THEMES = {
    "saffron": dict(bg="#FFF8F0",surface="#FEE4CC",card="#FFFFFF",border="#F5C9A0",
                    accent="#E8630A",accent2="#0EA5E9",accent3="#7C3AED",text="#1C0A00",
                    muted="#92614A",warning="#D97706",success="#10B981",error="#DC2626",
                    white="#FFFFFF",urgent="#DC2626"),
    "dark":    dict(bg="#0D1117",surface="#161B22",card="#1C2128",border="#30363D",
                    accent="#E8630A",accent2="#388BFD",accent3="#A78BFA",text="#E6EDF3",
                    muted="#8B949E",warning="#D29922",success="#2EA043",error="#F85149",
                    white="#FFFFFF",urgent="#FF4444"),
}
C = dict(THEMES["saffron"])

ZONES          = ["Zone A","Zone B","Zone C","Zone D"]
DONOR_TYPES    = ["HOTEL","HOSTEL","CATERING_SERVICE"]
RECEIVER_TYPES = ["NGO","ORPHANAGE"]
KG_PER_MEAL    = 0.4

# ══════════════════════════════════════════════════════════════
#  LANGUAGE PACKS  (Feature 20)
# ══════════════════════════════════════════════════════════════
LANG = {
    "en": dict(
        app_name="MealBridge", tagline="Connecting Food. Reducing Waste.",
        sign_in="SIGN IN", create_account="CREATE ACCOUNT", new_here="New to MealBridge?",
        demo="Demo: hotel_abc / pass123  |  helping_ngo / pass123",
        dashboard="Dashboard", profile="Profile", my_donations="My Donations",
        add_donation="Add Donation", my_requests="My Requests", new_request="New Request",
        matches="Matches", smart_match="Smart Match", zone_map="Zone Map",
        leaderboard="Leaderboard", history="History Log", statistics="Statistics",
        calendar="Calendar", logout="Logout",
        search_ph="Search donors, items, zones...",
        confirm_title="Confirm Submission", cancel="Cancel", confirm="Confirm",
        submit_donation="SUBMIT DONATION", submit_request="SUBMIT REQUEST",
        pickup_zone="PICKUP ZONE", food_items="FOOD ITEMS (up to 6)",
        qty_needed="QUANTITY NEEDED (meals)", zone_lbl="ZONE", urgency="URGENCY LEVEL",
        type_lbl="TYPE", i_am="I AM A", food_donor="Food Donor",
        food_receiver="Food Receiver", full_name="FULL NAME", contact="CONTACT",
        rerun="Re-run Matching", meals_saved="Meals Saved",
        total_donors="Total Donors", total_receivers="Total Receivers",
        active_matches="Active Matches", waste_prev="Waste Prevented",
        no_data="No data yet.", no_donations="No donations yet.",
        no_requests="No requests yet.", no_matches="No matches found yet.",
        export_csv="Export as CSV", export_json="Export as JSON",
        tip_add="Click here to add a donation!", tip_req="Click here to request food!",
        urgent_msg="donation(s) expiring in 3 hours — act now!",
        i_am_a="I AM A", username_lbl="USERNAME", password_lbl="PASSWORD",
        add_item="+ Add Another Item", refreshed="Dashboard auto-refreshed",
    ),
    "hi": dict(
        app_name="मीलब्रिज", tagline="भोजन जोड़ें। बर्बादी घटाएं।",
        sign_in="साइन इन", create_account="खाता बनाएं", new_here="नए हैं?",
        demo="डेमो: hotel_abc / pass123",
        dashboard="डैशबोर्ड", profile="प्रोफ़ाइल", my_donations="मेरे दान",
        add_donation="दान जोड़ें", my_requests="मेरी अनुरोध", new_request="नया अनुरोध",
        matches="मिलान", smart_match="स्मार्ट मिलान", zone_map="क्षेत्र नक्शा",
        leaderboard="लीडरबोर्ड", history="इतिहास", statistics="आंकड़े",
        calendar="कैलेंडर", logout="लॉगआउट",
        search_ph="खोजें...",
        confirm_title="पुष्टि करें", cancel="रद्द", confirm="पुष्टि",
        submit_donation="दान जमा करें", submit_request="अनुरोध जमा",
        pickup_zone="पिकअप क्षेत्र", food_items="खाद्य सामग्री",
        qty_needed="आवश्यक मात्रा", zone_lbl="क्षेत्र", urgency="आपातकाल",
        type_lbl="प्रकार", i_am="मैं हूँ", food_donor="दाता",
        food_receiver="प्राप्तकर्ता", full_name="पूरा नाम", contact="संपर्क",
        rerun="मिलान चलाएं", meals_saved="बचाए भोजन",
        total_donors="कुल दाता", total_receivers="कुल प्राप्तकर्ता",
        active_matches="सक्रिय मिलान", waste_prev="बर्बादी रोकी",
        no_data="डेटा नहीं।", no_donations="दान नहीं।",
        no_requests="अनुरोध नहीं।", no_matches="मिलान नहीं।",
        export_csv="CSV निर्यात", export_json="JSON निर्यात",
        tip_add="दान जोड़ने के लिए क्लिक करें!", tip_req="अनुरोध के लिए क्लिक करें!",
        urgent_msg="दान 3 घंटे में समाप्त!",
        i_am_a="मैं हूँ", username_lbl="उपयोगकर्ता नाम", password_lbl="पासवर्ड",
        add_item="+ और जोड़ें", refreshed="डैशबोर्ड अपडेट हुआ",
    ),
    "mr": dict(
        app_name="मीलब्रिज", tagline="अन्न जोडा. नासाडी कमी करा.",
        sign_in="साइन इन करा", create_account="खाते तयार करा", new_here="नवीन आहात?",
        demo="डेमो: hotel_abc / pass123",
        dashboard="डॅशबोर्ड", profile="प्रोफाइल", my_donations="माझे दान",
        add_donation="दान जोडा", my_requests="माझ्या विनंत्या", new_request="नवीन विनंती",
        matches="जुळणी", smart_match="स्मार्ट जुळणी", zone_map="क्षेत्र नकाशा",
        leaderboard="लीडरबोर्ड", history="इतिहास", statistics="आकडेवारी",
        calendar="दिनदर्शिका", logout="लॉगआउट",
        search_ph="शोधा...",
        confirm_title="निश्चित करा", cancel="रद्द", confirm="निश्चित",
        submit_donation="दान सादर करा", submit_request="विनंती सादर करा",
        pickup_zone="पिकअप क्षेत्र", food_items="अन्न वस्तू",
        qty_needed="आवश्यक प्रमाण", zone_lbl="क्षेत्र", urgency="तातडी",
        type_lbl="प्रकार", i_am="मी आहे", food_donor="दाता",
        food_receiver="प्राप्तकर्ता", full_name="पूर्ण नाव", contact="संपर्क",
        rerun="जुळणी पुन्हा", meals_saved="वाचवलेले जेवण",
        total_donors="एकूण दाते", total_receivers="एकूण प्राप्तकर्ते",
        active_matches="सक्रिय जुळण्या", waste_prev="नासाडी रोखली",
        no_data="डेटा नाही.", no_donations="दान नाही.",
        no_requests="विनंत्या नाहीत.", no_matches="जुळणी नाही.",
        export_csv="CSV निर्यात", export_json="JSON निर्यात",
        tip_add="दान जोडण्यासाठी क्लिक करा!", tip_req="विनंतीसाठी क्लिक करा!",
        urgent_msg="दान 3 तासात संपणार!",
        i_am_a="मी आहे", username_lbl="वापरकर्ता नाव", password_lbl="पासवर्ड",
        add_item="+ आणखी जोडा", refreshed="डॅशबोर्ड अपडेट झाला",
    ),
}
_LANG = "en"
_THEME = "saffron"

def T(k): return LANG.get(_LANG, LANG["en"]).get(k, LANG["en"].get(k, k))

# ══════════════════════════════════════════════════════════════
#  DATA STORE
# ══════════════════════════════════════════════════════════════
class DataStore:
    def __init__(self):
        self.users={}; self.donors={}; self.receivers={}
        self.donations=[]; self.requests=[]; self.matches=[]; self.history=[]
        self.stats={"total_meals":0,"total_matches":0}
        self._nid={"donor":1,"receiver":101,"donation":201,"request":301}
        self._seed()

    def _seed(self):
        for u,p,r,n,c,z,s,ug in [
            ("hotel_abc","pass123","donor","ABC Hotel","9876543210","Zone A","HOTEL",None),
            ("city_hostel","pass123","donor","City Hostel","9123456789","Zone B","HOSTEL",None),
            ("green_cat","pass123","donor","Green Catering","9000011111","Zone C","CATERING_SERVICE",None),
            ("helping_ngo","pass123","receiver","Helping NGO","9988776655","Zone A","NGO",3),
            ("hope_orphan","pass123","receiver","Hope Orphanage","8877665544","Zone B","ORPHANAGE",2),
            ("care_ngo","pass123","receiver","Care NGO","9111122222","Zone C","NGO",1),
        ]: self._reg(u,p,r,n,c,z,s,ug)
        now=datetime.now()
        for d in [
            {"id":201,"donor_id":1,"zone":"Zone A","items":[{"name":"Rice","qty":50,"expiry":5},{"name":"Bread","qty":30,"expiry":2}],"timestamp":"2025-07-01 10:00","created_ts":now-timedelta(hours=3)},
            {"id":202,"donor_id":2,"zone":"Zone B","items":[{"name":"Dal","qty":40,"expiry":6},{"name":"Chapati","qty":60,"expiry":3}],"timestamp":"2025-07-01 11:00","created_ts":now-timedelta(hours=2)},
            {"id":203,"donor_id":3,"zone":"Zone C","items":[{"name":"Pasta","qty":70,"expiry":2},{"name":"Juice","qty":20,"expiry":1}],"timestamp":"2025-07-01 12:00","created_ts":now-timedelta(hours=1)},
        ]:
            self.donations.append(d)
            dn=self.donors.get(d["donor_id"],{}).get("name","?")
            self.history.append({"time":d["timestamp"],"type":"DONATION","msg":f"Donation #{d["id"]} by {dn} ({d["zone"]})"})
        self._nid["donation"]=204
        for r in [
            {"id":301,"receiver_id":101,"qty":40,"urgency":3,"zone":"Zone A","item":"Rice","timestamp":"2025-07-01 10:30"},
            {"id":302,"receiver_id":102,"qty":50,"urgency":2,"zone":"Zone B","item":"Dal","timestamp":"2025-07-01 11:30"},
            {"id":303,"receiver_id":103,"qty":60,"urgency":1,"zone":"Zone C","item":"Pasta","timestamp":"2025-07-01 12:30"},
        ]:
            self.requests.append(r)
            rn=self.receivers.get(r["receiver_id"],{}).get("name","?")
            self.history.append({"time":r["timestamp"],"type":"REQUEST","msg":f"Request #{r["id"]} by {rn} ({r['item']}) urgency {r["urgency"]}"})
        self._nid["request"]=304
        self._run_matching()

    def _hash(self,pw): return hashlib.sha256(pw.encode()).hexdigest()
    def _reg(self,u,pw,role,name,contact,zone,stype=None,urgency=None):
        uid=self._nid[role]; self._nid[role]+=1
        self.users[u]={"username":u,"password":self._hash(pw),"role":role,"entity_id":uid}
        e={"id":uid,"name":name,"contact":contact,"zone":zone,"type":stype or "HOTEL"}
        if role=="receiver": e["urgency"]=urgency or 1
        (self.donors if role=="donor" else self.receivers)[uid]=e

    def register(self,u,pw,role,name,contact,zone,stype=None,urgency=None):
        if u in self.users: return False,"Username already exists."
        if not all([u,pw,name,contact,zone]): return False,"All fields required."
        self._reg(u,pw,role,name,contact,zone,stype,urgency)
        self._log("REGISTER",f"New {role}: {name}"); return True,"Registration successful!"

    def login(self,u,pw):
        usr=self.users.get(u)
        if not usr or usr["password"]!=self._hash(pw): return None
        self._log("LOGIN",f"Login: {u}"); return usr

    def add_donation(self,donor_id,zone,items):
        d={"id":self._nid["donation"],"donor_id":donor_id,"zone":zone,"items":items,
           "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M"),"created_ts":datetime.now()}
        self.donations.append(d); self._nid["donation"]+=1
        dn=self.donors.get(donor_id,{}).get("name","?")
        self._log("DONATION",f"Donation #{d["id"]} by {dn} in {zone}")
        self._run_matching(); return d["id"]

    def add_request(self,recv_id,qty,urgency,zone,item="Any"):
        item=(item or "Any").strip() or "Any"
        r={"id":self._nid["request"],"receiver_id":recv_id,"qty":qty,
           "urgency":urgency,"zone":zone,"item":item,"timestamp":datetime.now().strftime("%Y-%m-%d %H:%M")}
        self.requests.append(r); self._nid["request"]+=1
        rn=self.receivers.get(recv_id,{}).get("name","?")
        self._log("REQUEST",f"Request #{r["id"]} by {rn} {qty} meals ({item}) urgency {urgency}")
        self._run_matching(); return r["id"]

    def _log(self,typ,msg):
        self.history.append({"time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"type":typ,"msg":msg})

    def _expiry(self,d): return min((i["expiry"] for i in d["items"]),default=9999)
    def _qty(self,d): return sum(i["qty"] for i in d["items"])
    def _norm_item(self,item): return (item or "Any").strip().lower()
    def _disp_item(self,item): return (item or "Any").strip() or "Any"

    def _item_qty(self,donation,item):
        ni=self._norm_item(item)
        if ni=="any": return self._qty(donation)
        return sum(i["qty"] for i in donation["items"] if self._norm_item(i.get("name",""))==ni)

    def _run_matching(self):
        self.matches=[]
        sd=sorted(self.donations,key=self._expiry)
        sr=sorted(self.requests,key=lambda r:-r["urgency"])
        rr={r["id"]:r["qty"] for r in sr}
        rem={}
        for d in sd:
            items={}
            for it in d["items"]:
                k=self._norm_item(it.get("name",""))
                items[k]=items.get(k,0)+max(0,int(it.get("qty",0)))
            rem[d["id"]]={"total":sum(items.values()),"items":items}
        for req in sr:
            if rr.get(req["id"],0)<=0: continue
            req_item=self._norm_item(req.get("item","Any"))
            donors_sorted=sorted(sd,key=lambda d: 0 if d["zone"]==req["zone"] else 1)
            for don in donors_sorted:
                st=rem.get(don["id"],{"total":0,"items":{}})
                if st["total"]<=0: continue
                avail=st["total"] if req_item=="any" else st["items"].get(req_item,0)
                if avail<=0: continue
                alloc=min(avail,rr[req["id"]])
                if alloc<=0: continue
                if req_item=="any":
                    left=alloc
                    for item_name in list(st["items"].keys()):
                        if left<=0: break
                        take=min(st["items"][item_name],left)
                        st["items"][item_name]-=take
                        left-=take
                else:
                    st["items"][req_item]-=alloc
                st["total"]-=alloc
                dn=self.donors.get(don["donor_id"],{}).get("name","?")
                rn=self.receivers.get(req["receiver_id"],{}).get("name","?")
                parts=[]
                if self._expiry(don)<=2: parts.append("Critical expiry")
                elif self._expiry(don)<=5: parts.append("Near expiry")
                if req["urgency"]==3: parts.append("High urgency")
                elif req["urgency"]==2: parts.append("Medium urgency")
                if req_item!="any": parts.append("Item match")
                parts.append("Zone match" if don["zone"]==req["zone"] else "Cross-zone fallback")
                self.matches.append({"donation_id":don["id"],"request_id":req["id"],"donor_name":dn,
                    "receiver_name":rn,"zone":don["zone"],"meals":alloc,"urgency":req["urgency"],
                    "item":self._disp_item(req.get("item","Any")),
                    "reason":" · ".join(parts),"partial":alloc<avail or alloc<req["qty"]})
                rr[req["id"]]-=alloc
                if rr[req["id"]]<=0: break
        self.stats["total_matches"]=len(self.matches)
        self.stats["total_meals"]=sum(m["meals"] for m in self.matches)

    def get_smart(self):
        ud={m["donation_id"] for m in self.matches}; ur={m["request_id"] for m in self.matches}
        s=[]
        for req in self.requests:
            if req["id"] in ur: continue
            req_item=self._norm_item(req.get("item","Any"))
            for don in self.donations:
                if don["id"] in ud: continue
                if req_item!="any" and self._item_qty(don,req_item)<=0: continue
                exp=self._expiry(don); score=req["urgency"]*10+max(0,10-exp)
                if don["zone"]!=req["zone"]:
                    score-=3
                parts=[]
                if exp<=2: parts.append("Critical expiry")
                elif exp<=5: parts.append("Near expiry")
                if req["urgency"]==3: parts.append("High urgency")
                elif req["urgency"]==2: parts.append("Medium urgency")
                if req_item!="any": parts.append("Item match")
                parts.append("Zone match" if don["zone"]==req["zone"] else "Cross-zone fallback")
                s.append({"don":don,"req":req,"score":score,"reason":" · ".join(parts)})
        s.sort(key=lambda x:-x["score"]); return s[:3]

    def get_zone_map(self):
        zm={z:{"surplus":0,"demand":0,"donations":0,"requests":0} for z in ZONES}
        for d in self.donations:
            if d["zone"] in zm: zm[d["zone"]]["surplus"]+=self._qty(d); zm[d["zone"]]["donations"]+=1
        for r in self.requests:
            if r["zone"] in zm: zm[r["zone"]]["demand"]+=r["qty"]; zm[r["zone"]]["requests"]+=1
        return zm

    def get_leaderboard(self):
        lb={}
        for m in self.matches: lb[m["donor_name"]]=lb.get(m["donor_name"],0)+m["meals"]
        for d in self.donations:
            dn=self.donors.get(d["donor_id"],{}).get("name","?")
            if dn not in lb: lb[dn]=0
        return sorted(lb.items(),key=lambda x:-x[1])

    def get_trend(self):
        t={}
        for i in range(7): t[(datetime.now()-timedelta(days=6-i)).strftime("%m/%d")]=0
        for d in self.donations:
            try:
                day=datetime.strptime(d["timestamp"],"%Y-%m-%d %H:%M").strftime("%m/%d")
                if day in t: t[day]+=self._qty(d)
            except: pass
        return t

    def get_waste(self):
        kg=self.stats["total_meals"]*KG_PER_MEAL
        return {"kg":round(kg,1),"co2":round(kg*2.5,1),"meals":self.stats["total_meals"]}

    def get_urgent(self): return [d for d in self.donations if self._expiry(d)<=3]

    def is_donation_matched(self, donation_id):
        """Returns (matched:bool, receiver_name:str, meals:int)"""
        for m in self.matches:
            if m["donation_id"] == donation_id:
                return True, m["receiver_name"], m["meals"]
        return False, "", 0

    def is_request_matched(self, request_id):
        """Returns (matched:bool, donor_name:str, meals:int)"""
        for m in self.matches:
            if m["request_id"] == request_id:
                return True, m["donor_name"], m["meals"]
        return False, "", 0

    def is_donation_matched(self, donation_id):
        """Returns (matched:bool, receiver_name:str, meals:int)"""
        for m in self.matches:
            if m["donation_id"] == donation_id:
                return True, m["receiver_name"], m["meals"]
        return False, "", 0

    def is_request_matched(self, request_id):
        """Returns (matched:bool, donor_name:str, meals:int)"""
        for m in self.matches:
            if m["request_id"] == request_id:
                return True, m["donor_name"], m["meals"]
        return False, "", 0

    def get_cal(self,year,month):
        cal={}
        for d in self.donations:
            try:
                dt=datetime.strptime(d["timestamp"],"%Y-%m-%d %H:%M")
                if dt.year==year and dt.month==month:
                    cal[dt.day]=cal.get(dt.day,0)+self._qty(d)
            except: pass
        return cal

    def search(self,q):
        q=q.lower().strip()
        if not q: return []
        res=[]
        for d in self.donations:
            dn=self.donors.get(d["donor_id"],{}).get("name","")
            if q in dn.lower() or q in d["zone"].lower() or any(q in i["name"].lower() for i in d["items"]):
                res.append(("DON",f"Donation #{d["id"]} — {dn} ({d["zone"]})",d))
        for r in self.requests:
            rn=self.receivers.get(r["receiver_id"],{}).get("name","")
            if q in rn.lower() or q in r["zone"].lower() or q in r.get("item","any").lower():
                res.append(("REQ",f"Request #{r["id"]} — {rn} ({r["zone"]})",r))
        for uid,dn in self.donors.items():
            if q in dn["name"].lower() or q in dn["zone"].lower():
                res.append(("DNR",f"Donor: {dn["name"]} ({dn["zone"]})",dn))
        for uid,rn in self.receivers.items():
            if q in rn["name"].lower() or q in rn["zone"].lower():
                res.append(("RCV",f"Receiver: {rn["name"]} ({rn["zone"]})",rn))
        return res[:10]

    def get_stats(self):
        zd={}; uc={1:0,2:0,3:0}
        for d in self.donations: zd[d["zone"]]=zd.get(d["zone"],0)+self._qty(d)
        for r in self.requests: uc[r["urgency"]]=uc.get(r["urgency"],0)+1
        return {"total_donors":len(self.donors),"total_receivers":len(self.receivers),
                "total_donations":len(self.donations),"total_requests":len(self.requests),
                "total_matches":self.stats["total_matches"],"total_meals":self.stats["total_meals"],
                "zone_dist":zd,"urgency_counts":uc}

    def export_csv(self,path):
        with open(path,"w",newline="",encoding="utf-8") as f:
            w=csv.writer(f)
            w.writerow(["Type","ID","Zone","Name","Item","Meals","Urgency","Time"])
            for d in self.donations:
                dn=self.donors.get(d["donor_id"],{}).get("name","?")
                w.writerow(["DONATION",d["id"],d["zone"],dn,"Multiple",self._qty(d),"",d["timestamp"]])
            for r in self.requests:
                rn=self.receivers.get(r["receiver_id"],{}).get("name","?")
                w.writerow(["REQUEST",r["id"],r["zone"],rn,r.get("item","Any"),r["qty"],r["urgency"],r["timestamp"]])
            for m in self.matches:
                w.writerow(["MATCH",f"{m["donation_id"]}→{m["request_id"]}",m["zone"],
                            f"{m["donor_name"]}→{m["receiver_name"]}",m.get("item","Any"),m["meals"],m["urgency"],""])

    def export_json(self,path):
        def df(o): return o.isoformat() if isinstance(o,datetime) else str(o)
        with open(path,"w",encoding="utf-8") as f:
            json.dump({"donations":self.donations,"requests":self.requests,"matches":self.matches,
                       "history":self.history,"stats":self.stats,"exported":datetime.now().isoformat()},f,indent=2,default=df)

    def export_report(self,path):
        try:
            lines=["="*55,"  MEALBRIDGE — DONATION MATCH REPORT","="*55,
                   f"  Generated : {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                   f"  Donors    : {len(self.donors)}    Receivers: {len(self.receivers)}",
                   f"  Donations : {len(self.donations)}    Requests : {len(self.requests)}",
                   f"  Matches   : {self.stats["total_matches"]}    Meals    : {self.stats["total_meals"]}","="*55,"","MATCH RESULTS:","-"*55]
            for m in self.matches:
                t="[PARTIAL]" if m.get("partial") else "[FULL]   "
                lines+=[f"{t} {m['donor_name']} → {m['receiver_name']}",
                        f"         Zone:{m['zone']}  Meals:{m['meals']}  Urgency:{m['urgency']}",
                        f"         Why: {m.get('reason','')}","",""]
            lines+=["","DONATIONS:","-"*55]
            for d in self.donations:
                dn=self.donors.get(d["donor_id"],{}).get("name","?")
                lines.append(f"#{d["id"]}  {dn}  {d["zone"]}  {d["timestamp"]}")
                for it in d["items"]: lines.append(f"     {it["name"]}: {it["qty"]} meals, {it["expiry"]}h left")
            with open(path,"w",encoding="utf-8") as f: f.write("\n".join(lines))
            return True
        except: return False

# ══════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════
def _lt(h,a=0.2):
    h=h.lstrip("#"); r,g,b=int(h[0:2],16),int(h[2:4],16),int(h[4:6],16)
    return f"#{min(255,int(r+(255-r)*a)):02x}{min(255,int(g+(255-g)*a)):02x}{min(255,int(b+(255-b)*a)):02x}"

def _dk(h,a=0.12):
    h=h.lstrip("#"); r,g,b=int(h[0:2],16),int(h[2:4],16),int(h[4:6],16)
    return f"#{max(0,int(r*(1-a))):02x}{max(0,int(g*(1-a))):02x}{max(0,int(b*(1-a))):02x}"

def mk_entry(parent,ph="",show=None):
    f=tk.Frame(parent,bg=C["card"],highlightbackground=C["border"],highlightthickness=1,bd=0)
    e=tk.Entry(f,bg=C["card"],fg=C["muted"],insertbackground=C["accent"],font=("Courier New",12),bd=0,relief="flat",width=28)
    if show: e.config(show=show)
    e.insert(0,ph); e.pack(padx=12,pady=9,fill="x")
    if ph and not show:
        e.bind("<FocusIn>",lambda ev: (e.delete(0,"end"),e.config(fg=C["text"])) if e.get()==ph else None)
        e.bind("<FocusOut>",lambda ev: (e.insert(0,ph),e.config(fg=C["muted"])) if e.get()=="" else None)
    else: e.config(fg=C["text"])
    return f,e

def mk_btn(parent,text,cmd,color=None,width=20,fg=None,fs=12):
    bg=color or C["accent"]
    b=tk.Button(parent,text=text,command=cmd,bg=bg,fg=fg or C["white"],font=("Courier New",fs,"bold"),
                relief="flat",bd=0,cursor="hand2",activebackground=bg,activeforeground=C["white"],padx=16,pady=9,width=width)
    b.bind("<Enter>",lambda e,d=_dk(bg): b.config(bg=d))
    b.bind("<Leave>",lambda e: b.config(bg=bg))
    return b

def mk_combo(parent,values,width=26):
    s=ttk.Style(); s.theme_use("clam")
    s.configure("MB.TCombobox",fieldbackground=C["card"],background=C["surface"],foreground=C["text"],
                arrowcolor=C["accent"],bordercolor=C["border"],lightcolor=C["border"],darkcolor=C["border"],
                selectbackground=C["accent"],selectforeground=C["white"])
    s.map("MB.TCombobox",fieldbackground=[("readonly",C["card"])],foreground=[("readonly",C["text"])])
    cb=ttk.Combobox(parent,values=values,width=width,style="MB.TCombobox",font=("Courier New",11),state="readonly")
    cb.current(0); return cb

def sep_line(parent,pady=8): tk.Frame(parent,bg=C["border"],height=1).pack(fill="x",pady=pady)
def lbl(parent,text,size=11,color=None,bold=False,anchor="w",wrap=0):
    f=("Courier New",size,"bold") if bold else ("Courier New",size)
    kw={"wraplength":wrap} if wrap else {}
    return tk.Label(parent,text=text,bg=parent["bg"],fg=color or C["text"],font=f,anchor=anchor,**kw)

# ── Stat card with sparkline arrow (Feature 7) ──────────────────
def stat_card(parent,label,value,accent,icon="",sub=None,trend=0):
    f=tk.Frame(parent,bg=C["card"],highlightbackground=accent,highlightthickness=2,bd=0)
    tk.Frame(f,bg=accent,height=4).pack(fill="x")
    inner=tk.Frame(f,bg=C["card"]); inner.pack(fill="both",expand=True,padx=14,pady=10)
    top=tk.Frame(inner,bg=C["card"]); top.pack(fill="x")
    tk.Label(top,text=icon+" "+label,bg=C["card"],fg=C["muted"],font=("Courier New",8,"bold")).pack(side="left",anchor="w")
    if trend!=0:
        arrow="▲" if trend>0 else "▼"; tcol=C["success"] if trend>0 else C["error"]
        tk.Label(top,text=arrow,bg=C["card"],fg=tcol,font=("Courier New",11,"bold")).pack(side="right")
    tk.Label(inner,text=str(value),bg=C["card"],fg=C["text"],font=("Courier New",20,"bold")).pack(anchor="w",pady=(2,0))
    if sub: tk.Label(inner,text=sub,bg=C["card"],fg=accent,font=("Courier New",8)).pack(anchor="w")
    return f

# ══════════════════════════════════════════════════════════════
#  CHARTS
# ══════════════════════════════════════════════════════════════
def draw_bar(cv,data,w=360,h=200):
    cv.delete("all"); cv.config(bg=C["card"])
    if not data: return
    ml,mb,mt=50,40,20; cw=w-ml-20; ch=h-mb-mt; mv=max(data.values()) or 1; n=len(data)
    bw=max(10,(cw//n)-10)
    cv.create_line(ml,mt,ml,mt+ch,fill=C["border"],width=1)
    cv.create_line(ml,mt+ch,w-10,mt+ch,fill=C["border"],width=1)
    for i,(k,v) in enumerate(data.items()):
        bh=int((v/mv)*ch); x0=ml+i*(cw//n)+4; y0=mt+ch-bh; x1=x0+bw; y1=mt+ch
        # Feature 5: gradient bar orange→yellow
        for seg in range(max(bh,1)):
            ratio=seg/max(bh,1)
            r=int(0xe8+(0xf5-0xe8)*ratio); g=int(0x63+(0xc8-0x63)*ratio); b=int(0x0a+(0x42-0x0a)*ratio)
            cv.create_line(x0,y1-seg,x1,y1-seg,fill=f"#{r:02x}{g:02x}{b:02x}")
        cv.create_text((x0+x1)//2,y0-7,text=str(v),fill=C["text"],font=("Courier New",8,"bold"))
        cv.create_text((x0+x1)//2,y1+12,text=(k[:6] if len(k)>6 else k),fill=C["text"],font=("Courier New",8))

def draw_line(cv,data,w=380,h=180):
    cv.delete("all"); cv.config(bg=C["card"])
    if not data or max(data.values())==0: return
    col=C["accent2"]; ml,mb,mt=45,35,18; cw=w-ml-15; ch=h-mb-mt
    mv=max(data.values()) or 1; keys=list(data.keys()); n=len(keys)
    cv.create_line(ml,mt,ml,mt+ch,fill=C["border"],width=1)
    cv.create_line(ml,mt+ch,w-10,mt+ch,fill=C["border"],width=1)
    pts=[(ml+int(i*(cw/(n-1))) if n>1 else ml+cw//2, mt+ch-int((data[k]/mv)*ch)) for i,k in enumerate(keys)]
    for i,k in enumerate(keys):
        cv.create_text(pts[i][0],mt+ch+12,text=k,fill=C["muted"],font=("Courier New",7))
    if len(pts)>1:
        for i in range(len(pts)-1):
            cv.create_line(pts[i][0],pts[i][1],pts[i+1][0],pts[i+1][1],fill=col,width=2,smooth=True)
    for i,(x,y) in enumerate(pts):
        cv.create_oval(x-4,y-4,x+4,y+4,fill=col,outline=C["card"],width=2)
        if data[keys[i]]>0: cv.create_text(x,y-12,text=str(data[keys[i]]),fill=C["accent"],font=("Courier New",7,"bold"))

def draw_donut(cv,data,colors=None,w=200,h=200):
    cv.delete("all"); cv.config(bg=C["card"])
    cols=colors or [C["accent"],C["accent2"],C["accent3"]]
    total=sum(data.values())
    if not total: return
    cx,cy=w//2,h//2-10; ro=min(cx,cy)-18; ri=ro-36; start=0
    for i,(k,v) in enumerate(data.items()):
        ext=(v/total)*360
        cv.create_arc(cx-ro,cy-ro,cx+ro,cy+ro,start=start,extent=ext,fill=cols[i%len(cols)],outline=C["card"],width=2,style="pieslice")
        start+=ext
    cv.create_oval(cx-ri,cy-ri,cx+ri,cy+ri,fill=C["card"],outline="")
    cv.create_text(cx,cy-6,text=str(total),fill=C["accent"],font=("Courier New",14,"bold"))
    cv.create_text(cx,cy+10,text="Total",fill=C["text"],font=("Courier New",8))
    ly=6
    for i,(k,v) in enumerate(data.items()):
        pct=round(v/total*100)
        cv.create_rectangle(4,ly,13,ly+9,fill=cols[i%len(cols)],outline="")
        cv.create_text(16,ly+4,text=f"{k}:{pct}%",fill=C["text"],font=("Courier New",7),anchor="w")
        ly+=13

def draw_ring(cv,val,mx,color,w=110,h=110,label=""):
    # Feature 10: Progress rings
    cv.delete("all"); cv.config(bg=C["card"])
    cx,cy=w//2,h//2; r=min(cx,cy)-12
    cv.create_arc(cx-r,cy-r,cx+r,cy+r,start=0,extent=359,outline=C["border"],width=8,style="arc")
    pct=min(val/mx,1.0) if mx else 0
    if pct>0: cv.create_arc(cx-r,cy-r,cx+r,cy+r,start=90,extent=-(pct*359.9),outline=color,width=8,style="arc")
    cv.create_text(cx,cy-8,text=f"{round(pct*100)}%",fill=color,font=("Courier New",12,"bold"))
    if label: cv.create_text(cx,cy+10,text=label,fill=C["muted"],font=("Courier New",7))

# ══════════════════════════════════════════════════════════════
#  SCROLL FRAME
# ══════════════════════════════════════════════════════════════
class SF(tk.Frame):
    def __init__(self,parent,**kw):
        super().__init__(parent,**kw); self.config(bg=C["bg"])
        cv=tk.Canvas(self,bg=C["bg"],highlightthickness=0,bd=0)
        sb=tk.Scrollbar(self,orient="vertical",command=cv.yview,bg=C["surface"],troughcolor=C["bg"],relief="flat",bd=0)
        self.inner=tk.Frame(cv,bg=C["bg"])
        self.inner.bind("<Configure>",lambda e: cv.configure(scrollregion=cv.bbox("all")))
        cv.create_window((0,0),window=self.inner,anchor="nw",tags="inner")
        cv.configure(yscrollcommand=sb.set)
        cv.pack(side="left",fill="both",expand=True); sb.pack(side="right",fill="y")
        cv.bind("<Configure>",lambda e: cv.itemconfig("inner",width=e.width))
        cv.bind_all("<MouseWheel>",lambda e: cv.yview_scroll(int(-1*(e.delta/120)),"units"))

# ══════════════════════════════════════════════════════════════
#  REUSABLE UI COMPONENTS
# ══════════════════════════════════════════════════════════════
def empty_state(parent,icon,msg,hint=""):
    # Feature 18: Empty state illustrations
    f=tk.Frame(parent,bg=C["bg"]); f.pack(pady=36)
    cv=tk.Canvas(f,width=90,height=90,bg=C["bg"],highlightthickness=0); cv.pack()
    cv.create_oval(5,5,85,85,fill=C["surface"],outline=C["border"],width=2)
    cv.create_text(45,45,text=icon,font=("Segoe UI Emoji",26),fill=C["muted"])
    tk.Label(f,text=msg,bg=C["bg"],fg=C["muted"],font=("Courier New",12,"bold")).pack(pady=(8,4))
    if hint: tk.Label(f,text=hint,bg=C["bg"],fg=C["border"],font=("Courier New",9),wraplength=280).pack()

def confirm_dialog(root,title,msg,on_ok):
    # Feature 17: Confirmation dialog
    d=tk.Toplevel(root); d.title(""); d.configure(bg=C["bg"]); d.resizable(False,False); d.grab_set()
    w,h=450,230; sw=root.winfo_screenwidth(); sh=root.winfo_screenheight()
    d.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
    tk.Frame(d,bg=C["accent"],height=4).pack(fill="x")
    body=tk.Frame(d,bg=C["bg"]); body.pack(fill="both",expand=True,padx=28,pady=18)
    tk.Label(body,text=title,bg=C["bg"],fg=C["text"],font=("Courier New",14,"bold")).pack(anchor="w")
    tk.Frame(body,bg=C["border"],height=1).pack(fill="x",pady=8)
    tk.Label(body,text=msg,bg=C["bg"],fg=C["text"],font=("Courier New",11),wraplength=390,justify="left").pack(anchor="w",pady=(0,14))
    br=tk.Frame(body,bg=C["bg"]); br.pack(anchor="e")
    def do(): d.destroy(); on_ok()
    tk.Button(br,text=T("cancel"),command=d.destroy,bg=C["surface"],fg=C["muted"],
             font=("Courier New",11),relief="flat",bd=0,cursor="hand2",padx=16,pady=8).pack(side="left",padx=(0,8))
    tk.Button(br,text=T("confirm"),command=do,bg=C["accent"],fg=C["white"],
             font=("Courier New",11,"bold"),relief="flat",bd=0,cursor="hand2",padx=16,pady=8).pack(side="left")

# ══════════════════════════════════════════════════════════════
#  APP
# ══════════════════════════════════════════════════════════════
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.db=DataStore(); self.user=None
        self._theme=_THEME; self._sidebar_on=True
        self._alert_id=None; self._notif_win=None; self._search_pop=None
        self._tips_shown=set(); self._on_dash=False
        self.title("MealBridge"); self.geometry("1300x780"); self.minsize(960,620)
        self.configure(bg=C["bg"]); self.resizable(True,True)
        self._splash()

    def _clear(self):
        self.unbind("<Return>")
        for w in self.winfo_children(): w.destroy()

    def _center(self):
        self.update_idletasks(); sw=self.winfo_screenwidth(); sh=self.winfo_screenheight()
        self.geometry(f"+{(sw-self.winfo_width())//2}+{(sh-self.winfo_height())//2}")

    # ── Feature 2: SPLASH ──────────────────────────────────
    def _splash(self):
        self.geometry("480x320"); self._center(); self.overrideredirect(True)
        sp=tk.Frame(self,bg=C["surface"],highlightbackground=C["accent"],highlightthickness=3)
        sp.pack(fill="both",expand=True)
        tk.Label(sp,text="🌿",bg=C["surface"],font=("Segoe UI Emoji",48)).pack(pady=(26,0))
        tk.Label(sp,text=T("app_name"),bg=C["surface"],fg=C["accent"],font=("Courier New",28,"bold")).pack()
        tk.Label(sp,text=T("tagline"),bg=C["surface"],fg=C["muted"],font=("Courier New",10)).pack(pady=(4,18))
        bg_bar=tk.Frame(sp,bg=C["border"],height=6,width=300); bg_bar.pack()
        fill=tk.Frame(sp,bg=C["accent"],height=6,width=0); fill.place(in_=bg_bar,x=0,y=0)
        pl=tk.Label(sp,text="Initializing...",bg=C["surface"],fg=C["muted"],font=("Courier New",9)); pl.pack(pady=5)
        steps=[("Loading data...",25),("Running matching...",55),("Building UI...",80),("Almost done...",95),("Ready!",100)]
        def go(i=0):
            if i>=len(steps): self.after(180,self._done_splash); return
            msg,p=steps[i]; fill.config(width=int(300*p/100)); pl.config(text=msg); sp.update()
            self.after(310,lambda:go(i+1))
        self.after(120,go)

    def _done_splash(self):
        self.overrideredirect(False); self.geometry("1300x780"); self._center()
        self.unbind("<Return>"); self._login()

    # ── LOGIN ───────────────────────────────────────────────
    def _login(self):
        self._clear(); self.geometry("500x660"); self._center()
        root=tk.Frame(self,bg=C["bg"]); root.pack(fill="both",expand=True)
        tk.Frame(root,bg=C["accent"],width=6).pack(side="left",fill="y")
        body=tk.Frame(root,bg=C["bg"]); body.pack(side="left",fill="both",expand=True,padx=44,pady=34)
        logo=tk.Frame(body,bg=C["bg"]); logo.pack(pady=(0,22))
        tk.Label(logo,text="🌿",bg=C["bg"],font=("Segoe UI Emoji",42)).pack()
        tk.Label(logo,text=T("app_name"),bg=C["bg"],fg=C["accent"],font=("Courier New",28,"bold")).pack()
        tk.Label(logo,text=T("tagline"),bg=C["bg"],fg=C["muted"],font=("Courier New",10)).pack()
        # Language toggle (Feature 20)
        lf=tk.Frame(body,bg=C["bg"]); lf.pack(anchor="e",pady=(6,0))
        tk.Label(lf,text="🌐",bg=C["bg"],font=("Segoe UI Emoji",11)).pack(side="left",padx=(0,4))
        for code,name in [("en","EN"),("hi","हि"),("mr","म")]:
            def mklang(c=code):
                def fn():
                    global _LANG; _LANG=c; self._login()
                return fn
            tk.Button(lf,text=name,command=mklang(),
                     bg=C["accent"] if _LANG==code else C["surface"],
                     fg=C["white"] if _LANG==code else C["muted"],
                     font=("Courier New",9,"bold"),relief="flat",bd=0,cursor="hand2",padx=8,pady=3).pack(side="left",padx=2)
        sep_line(body)
        tk.Label(body,text=T("username_lbl"),bg=C["bg"],fg=C["muted"],font=("Courier New",9,"bold")).pack(anchor="w",pady=(12,2))
        f1,self._lu=mk_entry(body,"Enter username"); f1.pack(fill="x")
        tk.Label(body,text=T("password_lbl"),bg=C["bg"],fg=C["muted"],font=("Courier New",9,"bold")).pack(anchor="w",pady=(10,2))
        f2,self._lp=mk_entry(body,show="●"); f2.pack(fill="x")
        self._lerr=tk.Label(body,text="",bg=C["bg"],fg=C["error"],font=("Courier New",10)); self._lerr.pack(pady=6)
        mk_btn(body,T("sign_in"),self._do_login,color=C["accent"],width=28).pack(pady=4,fill="x")
        sep_line(body,pady=12)
        tk.Label(body,text=T("new_here"),bg=C["bg"],fg=C["muted"],font=("Courier New",10)).pack()
        mk_btn(body,T("create_account"),self._do_register,color=C["surface"],width=28,fg=C["accent2"],fs=11).pack(pady=6,fill="x")
        tk.Label(body,text=T("demo"),bg=C["bg"],fg=C["border"],font=("Courier New",8)).pack(pady=(14,0))
        self.bind("<Return>",lambda e:self._do_login())

    def _do_login(self):
        u=self.db.login(self._lu.get().strip(),self._lp.get().strip())
        if not u: self._lerr.config(text="⚠  Invalid credentials"); return
        self.user=u; self._main()

    # ── REGISTER ────────────────────────────────────────────
    def _do_register(self):
        self._clear(); self.geometry("600x840"); self._center()
        outer=tk.Frame(self,bg=C["bg"]); outer.pack(fill="both",expand=True)
        tk.Frame(outer,bg=C["accent2"],width=6).pack(side="left",fill="y")
        sf=SF(outer); sf.pack(side="left",fill="both",expand=True)
        body=sf.inner; body.config(padx=44,pady=28)
        lbl(body,T("create_account"),size=22,bold=True).pack(anchor="w")
        lbl(body,T("tagline"),size=10,color=C["muted"]).pack(anchor="w",pady=(2,14)); sep_line(body)
        rv=tk.StringVar(value="donor")
        lbl(body,T("i_am_a"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(12,6))
        rf=tk.Frame(body,bg=C["bg"]); rf.pack(anchor="w")
        sf2=tk.Frame(body,bg=C["bg"]); uf=tk.Frame(body,bg=C["bg"])
        sub_cb=mk_combo(sf2,DONOR_TYPES); urg_cb=mk_combo(uf,["1 - Low","2 - Medium","3 - High"])
        def upd():
            if rv.get()=="donor": sub_cb.config(values=DONOR_TYPES); sub_cb.current(0); uf.pack_forget(); sf2.pack(anchor="w",pady=(0,8))
            else: sub_cb.config(values=RECEIVER_TYPES); sub_cb.current(0); sf2.pack(anchor="w",pady=(0,8)); uf.pack(anchor="w",pady=(0,8))
        for val,txt in [("donor",T("food_donor")),("receiver",T("food_receiver"))]:
            tk.Radiobutton(rf,text=txt,variable=rv,value=val,command=upd,bg=C["bg"],fg=C["text"],
                          selectcolor=C["surface"],activebackground=C["bg"],font=("Courier New",11)).pack(side="left",padx=(0,20))
        fields=[]
        for lk,ph,pw in [(T("full_name"),"e.g. ABC Hotel",False),("USERNAME","choose a username",False),
                          ("PASSWORD","min 6 characters",True),(T("contact"),"10-digit number",False)]:
            lbl(body,lk,size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(12,2))
            fr,en=mk_entry(body,ph,show=("●" if pw else None)); fr.pack(fill="x"); fields.append(en)
        lbl(body,T("zone_lbl"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(12,4))
        zc=mk_combo(body,ZONES); zc.pack(anchor="w")
        lbl(sf2,T("type_lbl"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(0,4))
        sub_cb.pack(anchor="w"); sf2.pack(anchor="w",pady=(12,0))
        lbl(uf,T("urgency"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(0,4)); urg_cb.pack(anchor="w")
        el=lbl(body,"",size=10,color=C["error"]); el.pack(pady=8)
        def do_reg():
            nm=fields[0].get().strip(); un=fields[1].get().strip()
            pw=fields[2].get().strip(); ct=fields[3].get().strip()
            role=rv.get(); st=sub_cb.get(); ug=int(urg_cb.get()[0]) if role=="receiver" else None
            ok,msg=self.db.register(un,pw,role,nm,ct,zc.get(),st,ug)
            if ok: messagebox.showinfo("Success","✅ "+msg); self._login()
            else: el.config(text="⚠  "+msg)
        mk_btn(body,T("create_account"),do_reg,color=C["accent2"],width=28).pack(pady=10,fill="x")
        mk_btn(body,"← Back",self._login,color=C["surface"],width=28,fg=C["muted"],fs=10).pack(fill="x")

    # ── MAIN SHELL ──────────────────────────────────────────
    def _main(self):
        self._clear(); self.geometry("1300x780"); self._center()
        # TOPBAR
        tb=tk.Frame(self,bg=C["surface"],height=50); tb.pack(fill="x"); tb.pack_propagate(False)
        # Feature 3: sidebar toggle button
        tk.Button(tb,text="☰",bg=C["surface"],fg=C["accent"],font=("Courier New",16,"bold"),
                 relief="flat",bd=0,cursor="hand2",command=self._tog_sidebar,padx=10).pack(side="left",pady=6)
        tk.Label(tb,text="🌿 "+T("app_name"),bg=C["surface"],fg=C["accent"],font=("Courier New",13,"bold")).pack(side="left",padx=(2,14),pady=10)
        tk.Label(tb,text=T("tagline"),bg=C["surface"],fg=C["muted"],font=("Courier New",9)).pack(side="left",pady=10)
        # Feature 11: Search bar
        sbx=tk.Frame(tb,bg=C["surface"]); sbx.pack(side="left",padx=16,pady=8)
        sb_frame=tk.Frame(sbx,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); sb_frame.pack()
        tk.Label(sb_frame,text="🔍",bg=C["card"],font=("Segoe UI Emoji",10)).pack(side="left",padx=(8,0))
        self._sv=tk.StringVar(); self._sent=tk.Entry(sb_frame,textvariable=self._sv,bg=C["card"],fg=C["muted"],
                                                      insertbackground=C["accent"],font=("Courier New",10),bd=0,relief="flat",width=26)
        self._sent.insert(0,T("search_ph")); self._sent.pack(side="left",padx=(4,8),pady=6)
        self._sent.bind("<FocusIn>",self._s_in); self._sent.bind("<FocusOut>",self._s_out)
        self._sv.trace("w",lambda *a: self._do_search())
        # Right controls
        rc=tk.Frame(tb,bg=C["surface"]); rc.pack(side="right",padx=10)
        self._clk=tk.Label(rc,text="",bg=C["surface"],fg=C["text"],font=("Courier New",10,"bold")); self._clk.pack(side="right",padx=10)
        # Feature 14: Theme toggle
        self._tbtn=tk.Button(rc,text="🌙" if self._theme=="saffron" else "☀",bg=C["surface"],fg=C["text"],
                            font=("Segoe UI Emoji",13),relief="flat",bd=0,cursor="hand2",command=self._tog_theme,padx=6)
        self._tbtn.pack(side="right",padx=4)
        # Feature 15: Notifications bell
        nc=len([h for h in self.db.history[-40:] if h["type"] in ("DONATION","MATCH","REQUEST")])
        self._nbtn=tk.Button(rc,text=f"🔔{nc}",bg=C["surface"],fg=C["text"],font=("Courier New",10),
                            relief="flat",bd=0,cursor="hand2",command=self._notifs,padx=8,pady=6)
        self._nbtn.pack(side="right",padx=4)
        # Feature 20: Language buttons in topbar
        for code,name in [("en","EN"),("hi","हि"),("mr","म")]:
            def mklang2(c=code):
                def fn():
                    global _LANG; _LANG=c; self._main()
                return fn
            tk.Button(rc,text=name,command=mklang2(),
                     bg=C["surface"],fg=C["accent"] if _LANG==code else C["muted"],
                     font=("Courier New",8,"bold"),relief="flat",bd=0,cursor="hand2",padx=4).pack(side="right")
        self._tick()
        # BODY
        body_f=tk.Frame(self,bg=C["bg"]); body_f.pack(fill="both",expand=True)
        # SIDEBAR
        self._sb=tk.Frame(body_f,bg=C["surface"],width=210); self._sb.pack(side="left",fill="y"); self._sb.pack_propagate(False)
        ub=tk.Frame(self._sb,bg=C["white"],highlightbackground=C["accent"],highlightthickness=2); ub.pack(fill="x",padx=10,pady=10)
        rcol=C["accent"] if self.user["role"]=="donor" else C["accent2"]
        tk.Label(ub,text=self.user["username"],bg=C["white"],fg=C["text"],font=("Courier New",11,"bold")).pack(anchor="w",padx=10,pady=(10,2))
        txt="🟠 "+T("food_donor") if self.user["role"]=="donor" else "🔵 "+T("food_receiver")
        tk.Label(ub,text=txt,bg=C["white"],fg=rcol,font=("Courier New",9,"bold")).pack(anchor="w",padx=10,pady=(0,8))
        tk.Frame(self._sb,bg=C["border"],height=1).pack(fill="x")
        self._content=tk.Frame(body_f,bg=C["bg"]); self._content.pack(side="left",fill="both",expand=True)
        self._nav_btns={}
        role=self.user["role"]
        nav=[("📊",T("dashboard"),self._pg_dash),("👤",T("profile"),self._pg_profile)]
        if role=="donor": nav+=[("🍱",T("my_donations"),self._pg_my_don),("➕",T("add_donation"),self._pg_add_don)]
        else: nav+=[("📋",T("my_requests"),self._pg_my_req),("📝",T("new_request"),self._pg_new_req)]
        nav+=[("👥","All Members",self._pg_all_members),("🔗",T("matches"),self._pg_matches),("🧠",T("smart_match"),self._pg_smart),
              ("🗺",T("zone_map"),self._pg_zone),("📅",T("calendar"),self._pg_cal),
              ("🏆",T("leaderboard"),self._pg_lb),("📜",T("history"),self._pg_hist),
              ("📈",T("statistics"),self._pg_stats)]
        for ic,lb2,cmd in nav: self._nav_btns[lb2]=self._mk_nav(self._sb,ic,lb2,cmd)
        tk.Frame(self._sb,bg=C["surface"]).pack(fill="both",expand=True)
        tk.Frame(self._sb,bg=C["border"],height=1).pack(fill="x")
        tk.Button(self._sb,text="⬅  "+T("logout"),bg=C["surface"],fg=C["error"],
                 font=("Courier New",10,"bold"),relief="flat",bd=0,cursor="hand2",
                 activebackground=C["error"],activeforeground=C["white"],command=self._logout,pady=12).pack(fill="x")
        # Feature 19: Keyboard shortcuts
        self._bind_keys()
        self._alert_loop()
        self._pg_dash()

    def _mk_nav(self,parent,icon,label,cmd):
        def click(): self._set_nav(label); cmd()
        b=tk.Button(parent,text=f"  {icon}  {label}",bg=C["surface"],fg=C["muted"],
                    font=("Courier New",10),relief="flat",bd=0,cursor="hand2",anchor="w",
                    activebackground=C["border"],activeforeground=C["accent"],command=click,pady=11)
        b.pack(fill="x"); return b

    def _set_nav(self,label):
        for k,b in self._nav_btns.items():
            if k==label: b.config(bg=C["white"],fg=C["accent"],font=("Courier New",10,"bold"))
            else: b.config(bg=C["surface"],fg=C["muted"],font=("Courier New",10))

    # Feature 3: Sidebar slide
    def _tog_sidebar(self):
        if self._sidebar_on: self._sb.pack_forget(); self._sidebar_on=False
        else: self._sb.pack(side="left",fill="y",before=self._content); self._sidebar_on=True

    # Feature 14: Theme toggle
    def _tog_theme(self):
        global C,_THEME
        self._theme="dark" if self._theme=="saffron" else "saffron"
        _THEME=self._theme; C.update(THEMES[self._theme]); self._main()

    # Feature 15: Notifications panel
    def _notifs(self):
        if self._notif_win and self._notif_win.winfo_exists(): self._notif_win.destroy(); self._notif_win=None; return
        w=tk.Toplevel(self); w.overrideredirect(True); w.configure(bg=C["card"]); w.attributes("-topmost",True)
        self.update_idletasks()
        bx=self._nbtn.winfo_rootx(); by=self._nbtn.winfo_rooty()+42
        w.geometry(f"320x380+{bx-240}+{by}")
        tk.Frame(w,bg=C["accent"],height=3).pack(fill="x")
        hdr=tk.Frame(w,bg=C["surface"]); hdr.pack(fill="x")
        tk.Label(hdr,text="🔔  Notifications",bg=C["surface"],fg=C["text"],font=("Courier New",10,"bold")).pack(side="left",padx=12,pady=8)
        tk.Button(hdr,text="✕",bg=C["surface"],fg=C["muted"],font=("Courier New",10),relief="flat",bd=0,cursor="hand2",command=w.destroy).pack(side="right",padx=8)
        sf_n=SF(w); sf_n.pack(fill="both",expand=True)
        tc={"DONATION":C["accent"],"MATCH":C["success"],"REQUEST":C["accent2"],"REGISTER":C["warning"]}
        recent=[h for h in self.db.history[::-1] if h["type"] in tc][:15]
        for h in recent:
            row=tk.Frame(sf_n.inner,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); row.pack(fill="x",pady=1)
            inner=tk.Frame(row,bg=C["card"]); inner.pack(fill="x",padx=10,pady=7)
            col=tc.get(h["type"],C["muted"])
            tk.Label(inner,text=f" {h["type"][:3]} ",bg=col,fg=C["white"],font=("Courier New",7,"bold"),padx=3).pack(side="left")
            txt=h["msg"][:38]+"…" if len(h["msg"])>38 else h["msg"]
            tk.Label(inner,text=txt,bg=C["card"],fg=C["text"],font=("Courier New",9)).pack(side="left",padx=6)
        self._notif_win=w

    # Feature 11: Search
    def _s_in(self,ev):
        if self._sent.get()==T("search_ph"): self._sent.delete(0,"end"); self._sent.config(fg=C["text"])
    def _s_out(self,ev):
        if self._sent.get()=="": self._sent.insert(0,T("search_ph")); self._sent.config(fg=C["muted"])
        self.after(160,self._close_search)
    def _close_search(self):
        if self._search_pop:
            try: self._search_pop.destroy()
            except: pass
            self._search_pop=None
    def _do_search(self):
        q=self._sv.get()
        if q==T("search_ph") or len(q)<2: self._close_search(); return
        results=self.db.search(q); self._close_search()
        if not results: return
        w=tk.Toplevel(self); w.overrideredirect(True); w.configure(bg=C["card"]); w.attributes("-topmost",True)
        ex=self._sent.winfo_rootx(); ey=self._sent.winfo_rooty()+32
        w.geometry(f"360x{min(36+len(results)*36,280)}+{ex}+{ey}")
        tc={"DON":C["accent"],"REQ":C["accent2"],"DNR":C["warning"],"RCV":C["success"]}
        for typ,text,_ in results:
            row=tk.Frame(w,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); row.pack(fill="x",pady=1)
            inner=tk.Frame(row,bg=C["card"]); inner.pack(fill="x",padx=8,pady=5)
            col=tc.get(typ,C["muted"])
            tk.Label(inner,text=f" {typ} ",bg=col,fg=C["white"],font=("Courier New",7,"bold"),padx=3).pack(side="left")
            tk.Label(inner,text=text[:44],bg=C["card"],fg=C["text"],font=("Courier New",9)).pack(side="left",padx=6)
        self._search_pop=w

    # Feature 19: Keyboard shortcuts
    def _bind_keys(self):
        if self.user["role"]=="donor": self.bind("<Control-d>",lambda e:self._pg_add_don())
        else: self.bind("<Control-r>",lambda e:self._pg_new_req())
        self.bind("<Control-m>",lambda e:self._pg_matches())
        self.bind("<Control-l>",lambda e:self._logout())
        self.bind("<Control-s>",lambda e:self._pg_stats())

    def _logout(self):
        if self._alert_id: self.after_cancel(self._alert_id)
        self.user=None; self._login()

    def _tick(self):
        try: self._clk.config(text=datetime.now().strftime("%d %b  %H:%M:%S")); self.after(1000,self._tick)
        except: pass

    def _pg_frame(self,title,subtitle):
        for w in self._content.winfo_children(): w.destroy()
        sf=SF(self._content); sf.pack(fill="both",expand=True)
        page=sf.inner; page.config(bg=C["bg"],padx=30,pady=22)
        lbl(page,title,size=20,bold=True).pack(anchor="w")
        lbl(page,subtitle,size=10,color=C["muted"]).pack(anchor="w",pady=(2,12))
        sep_line(page); return page

    def _toast(self,msg,col=None):
        c=col or C["accent"]
        t=tk.Toplevel(self); t.overrideredirect(True); t.attributes("-topmost",True); t.configure(bg=c)
        tk.Label(t,text=f"  {msg}  ",bg=c,fg=C["white"],font=("Courier New",10,"bold"),padx=14,pady=8).pack()
        self.update_idletasks(); sw=self.winfo_screenwidth(); sh=self.winfo_screenheight()
        t.update_idletasks(); t.geometry(f"+{sw-t.winfo_width()-20}+{sh-72}")
        self.after(3000,lambda: self._close_t(t))
    def _close_t(self,t):
        try: t.destroy()
        except: pass

    # Feature 16: Onboarding tooltip
    def _tip(self,widget,text,key):
        if key in self._tips_shown: return
        self._tips_shown.add(key)
        t=tk.Toplevel(self); t.overrideredirect(True); t.attributes("-topmost",True); t.configure(bg=C["accent"])
        tk.Label(t,text=f"💡 {text}",bg=C["accent"],fg=C["white"],font=("Courier New",9,"bold"),padx=10,pady=6).pack()
        self.update_idletasks()
        try: x=widget.winfo_rootx()+widget.winfo_width()//2-80; y=widget.winfo_rooty()-36; t.geometry(f"+{x}+{y}")
        except: pass
        self.after(3200,lambda: self._close_t(t))

    # Urgent alert
    def _alert_loop(self):
        urgent=self.db.get_urgent()
        if urgent: self._toast(f"🔔 {len(urgent)} {T('urgent_msg')}",col=C["urgent"])
        self._alert_id=self.after(60000,self._alert_loop)

    # Feature 6: Auto refresh
    def _sched_refresh(self):
        if hasattr(self,"_ref_id"): self.after_cancel(self._ref_id)
        self._ref_id=self.after(30000,self._auto_ref)
    def _auto_ref(self):
        try:
            if self._on_dash: self._render_dash()
            self._sched_refresh()
        except: pass

    # ══════════════════════════════════════════
    #  DASHBOARD
    # ══════════════════════════════════════════
    def _pg_dash(self):
        self._set_nav(T("dashboard")); self._on_dash=True; self._render_dash(); self._sched_refresh()

    def _render_dash(self):
        for w in self._content.winfo_children(): w.destroy()
        sf=SF(self._content); sf.pack(fill="both",expand=True)
        page=sf.inner; page.config(bg=C["bg"],padx=30,pady=22)
        stats=self.db.get_stats(); waste=self.db.get_waste(); urgent=self.db.get_urgent()
        lbl(page,T("dashboard"),size=20,bold=True).pack(anchor="w")
        lbl(page,datetime.now().strftime("%A, %d %B %Y"),size=10,color=C["muted"]).pack(anchor="w",pady=(2,12))
        sep_line(page)
        if urgent:
            bn=tk.Frame(page,bg=C["urgent"]); bn.pack(fill="x",pady=(8,4))
            tk.Label(bn,text=f"  🔔  {len(urgent)} {T('urgent_msg')}",bg=C["urgent"],fg=C["white"],font=("Courier New",10,"bold"),pady=10).pack(anchor="w")
        # KPI + sparklines (Feature 7)
        g=tk.Frame(page,bg=C["bg"]); g.pack(fill="x",pady=(12,6))
        td=self.db.get_trend(); vals=list(td.values())
        tr=1 if len(vals)>1 and vals[-1]>vals[-2] else -1 if len(vals)>1 and vals[-1]<vals[-2] else 0
        kpis=[(T("total_donors"),stats["total_donors"],C["accent"],"🏷",None,0),
              (T("total_receivers"),stats["total_receivers"],C["accent2"],"🤝",None,0),
              (T("meals_saved"),stats["total_meals"],C["success"],"🍽","this session",tr),
              (T("active_matches"),stats["total_matches"],C["warning"],"🔗",None,tr),
              (T("waste_prev"),f"{waste["kg"]}kg",C["accent3"],"♻",f"~{waste["co2"]}kg CO₂",0)]
        for i,(lb2,v,col,ic,sub,trd) in enumerate(kpis):
            stat_card(g,lb2,v,col,ic,sub,trd).grid(row=0,column=i,padx=5,pady=4,sticky="nsew")
            g.columnconfigure(i,weight=1)
        sep_line(page)
        two=tk.Frame(page,bg=C["bg"]); two.pack(fill="x",pady=6)
        mc=tk.Frame(two,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); mc.grid(row=0,column=0,padx=(0,8),sticky="nsew")
        tk.Label(mc,text="Recent Matches",bg=C["card"],fg=C["text"],font=("Courier New",12,"bold")).pack(anchor="w",padx=14,pady=(12,4))
        tk.Frame(mc,bg=C["border"],height=1).pack(fill="x")
        if self.db.matches:
            for m in self.db.matches[-5:][::-1]: self._mrow(mc,m)
        else: empty_state(mc,"🔗",T("no_matches"),"Add donations and requests to begin")
        tc2=tk.Frame(two,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); tc2.grid(row=0,column=1,padx=(8,0),sticky="nsew")
        tk.Label(tc2,text="📈 7-Day Trend",bg=C["card"],fg=C["text"],font=("Courier New",12,"bold")).pack(anchor="w",padx=14,pady=(12,4))
        cv=tk.Canvas(tc2,width=360,height=180,bg=C["card"],highlightthickness=0,bd=0); cv.pack(padx=8,pady=(0,12))
        draw_line(cv,td,w=360,h=180)
        two.columnconfigure(0,weight=1); two.columnconfigure(1,weight=1)
        # Feature 16: tooltip
        key=T("add_donation") if self.user["role"]=="donor" else T("new_request")
        tip_txt=T("tip_add") if self.user["role"]=="donor" else T("tip_req")
        if key in self._nav_btns: self.after(900,lambda: self._tip(self._nav_btns[key],tip_txt,"first"))

    def _mrow(self,parent,m):
        uc={1:C["muted"],2:C["warning"],3:C["error"]}; ul={1:"LOW",2:"MED",3:"HI"}
        f=tk.Frame(parent,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); f.pack(fill="x",pady=1)
        inner=tk.Frame(f,bg=C["card"]); inner.pack(fill="x",padx=12,pady=7)
        left=tk.Frame(inner,bg=C["card"]); left.pack(side="left",fill="x",expand=True)
        p=" (partial)" if m.get("partial") else ""
        tk.Label(left,text=f"✅  {m["donor_name"]}  →  {m["receiver_name"]}{p}",bg=C["card"],fg=C["text"],font=("Courier New",10,"bold")).pack(anchor="w")
        tk.Label(left,text=f"Zone:{m["zone"]}  •  {m["meals"]} meals  •  {m.get('reason','')[:40]}",bg=C["card"],fg=C["muted"],font=("Courier New",8)).pack(anchor="w")
        urg=m.get("urgency",1)
        tk.Label(inner,text=f" {ul.get(urg,'?')} ",bg=uc.get(urg,C["muted"]),fg=C["white"],font=("Courier New",8,"bold"),padx=5,pady=2).pack(side="right")

    # ══════════════════════════════════════════
    #  PROFILE
    # ══════════════════════════════════════════
    def _pg_profile(self):
        self._set_nav(T("profile")); self._on_dash=False
        page=self._pg_frame(T("profile"),"Your account information")
        role=self.user["role"]; eid=self.user["entity_id"]
        entity=(self.db.donors if role=="donor" else self.db.receivers).get(eid,{})
        card=tk.Frame(page,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); card.pack(fill="x",pady=14)
        tk.Frame(card,bg=C["accent"] if role=="donor" else C["accent2"],height=4).pack(fill="x")
        inner=tk.Frame(card,bg=C["white"]); inner.pack(fill="x",padx=24,pady=18)
        rows=[("Username",self.user["username"]),("Role",role.capitalize()),("Name",entity.get("name","-")),
              ("Contact",entity.get("contact","-")),("Zone",entity.get("zone","-")),("Type",entity.get("type","-"))]
        if role=="receiver": rows.append(("Urgency",{1:"Low",2:"Medium",3:"High"}.get(entity.get("urgency",1),"-")))
        for k,v in rows:
            r=tk.Frame(inner,bg=C["white"]); r.pack(fill="x",pady=3)
            tk.Label(r,text=k+":",bg=C["white"],fg=C["muted"],font=("Courier New",10,"bold"),width=12,anchor="w").pack(side="left")
            tk.Label(r,text=v,bg=C["white"],fg=C["text"],font=("Courier New",10)).pack(side="left")

    # ══════════════════════════════════════════
    #  MY DONATIONS  (Feature 4: hover)
    # ══════════════════════════════════════════
    def _pg_my_don(self):
        self._set_nav(T("my_donations")); self._on_dash=False
        eid=self.user["entity_id"]; my=[d for d in self.db.donations if d["donor_id"]==eid]
        page=self._pg_frame(T("my_donations"),f"{len(my)} donation(s) recorded")
        if not my: empty_state(page,"🍱",T("no_donations"),"Use 'Add Donation' in the sidebar"); return
        for don in my[::-1]: self._don_card(page,don)

    def _don_card(self,parent,don):
        exp=self.db._expiry(don); bc=C["urgent"] if exp<=3 else C["accent"]
        f=tk.Frame(parent,bg=C["card"],highlightbackground=bc,highlightthickness=1); f.pack(fill="x",pady=5)
        # Feature 4: hover animation
        f.bind("<Enter>",lambda e: f.config(highlightbackground=C["warning"],highlightthickness=2))
        f.bind("<Leave>",lambda e: f.config(highlightbackground=bc,highlightthickness=1))
        tk.Frame(f,bg=bc,height=3).pack(fill="x")
        inner=tk.Frame(f,bg=C["card"]); inner.pack(fill="x",padx=16,pady=12)
        hdr=tk.Frame(inner,bg=C["card"]); hdr.pack(fill="x")
        tk.Label(hdr,text="Donation #"+str(don["id"]),bg=C["card"],fg=C["text"],font=("Courier New",12,"bold")).pack(side="left")
        ecol=C["urgent"] if exp<=2 else C["warning"] if exp<=5 else C["muted"]
        tk.Label(hdr,text=f"⏱ {exp}h"+(" ⚠URGENT" if exp<=3 else ""),bg=ecol,fg=C["white"],font=("Courier New",8,"bold"),padx=6,pady=3).pack(side="right")
        # Match status badge
        matched, recv_name, meals = self.db.is_donation_matched(don["id"])
        status_row = tk.Frame(inner,bg=C["card"]); status_row.pack(fill="x",pady=(4,2))
        if matched:
            tk.Label(status_row,text="✅ MATCHED",bg=C["success"],fg=C["white"],
                    font=("Courier New",8,"bold"),padx=8,pady=3).pack(side="left")
            tk.Label(status_row,text=f"  →  {recv_name}  •  {meals} meals allocated",
                    bg=C["card"],fg=C["success"],font=("Courier New",9,"bold")).pack(side="left")
        else:
            tk.Label(status_row,text="⏳ PENDING",bg=C["warning"],fg=C["white"],
                    font=("Courier New",8,"bold"),padx=8,pady=3).pack(side="left")
            tk.Label(status_row,text="  Waiting for a matching request (same zone preferred)",
                    bg=C["card"],fg=C["muted"],font=("Courier New",9)).pack(side="left")
        tk.Label(inner,text="Zone:"+don["zone"]+"  •  "+don["timestamp"],bg=C["card"],fg=C["muted"],font=("Courier New",9)).pack(anchor="w",pady=(2,6))
        tk.Frame(inner,bg=C["border"],height=1).pack(fill="x")
        for item in don["items"]:
            r=tk.Frame(inner,bg=C["card"]); r.pack(fill="x",pady=2)
            tk.Label(r,text=f"🍽  {item["name"]}",bg=C["card"],fg=C["text"],font=("Courier New",10)).pack(side="left")
            ic=C["urgent"] if item["expiry"]<=2 else C["muted"]
            tk.Label(r,text=f"Qty:{item["qty"]}  Exp:{item["expiry"]}h",bg=C["card"],fg=ic,font=("Courier New",9)).pack(side="right")

    # ══════════════════════════════════════════
    #  ADD DONATION  (Feature 17: confirm)
    # ══════════════════════════════════════════
    def _pg_add_don(self):
        self._set_nav(T("add_donation")); self._on_dash=False
        page=self._pg_frame(T("add_donation"),"Register food available for donation")
        form=tk.Frame(page,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); form.pack(fill="x",pady=14)
        tk.Frame(form,bg=C["accent"],height=4).pack(fill="x")
        inner=tk.Frame(form,bg=C["card"]); inner.pack(fill="x",padx=28,pady=20)
        lbl(inner,T("pickup_zone"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(0,4))
        zc=mk_combo(inner,ZONES); zc.pack(anchor="w")
        sep_line(inner,pady=10)
        lbl(inner,T("food_items"),size=9,color=C["muted"],bold=True).pack(anchor="w")
        items_f=tk.Frame(inner,bg=C["card"]); items_f.pack(fill="x",pady=6); irows=[]
        def add_row():
            if len(irows)>=6: return
            row=tk.Frame(items_f,bg=C["surface"],highlightbackground=C["border"],highlightthickness=1); row.pack(fill="x",pady=2)
            ir=tk.Frame(row,bg=C["surface"]); ir.pack(fill="x",padx=6,pady=6)
            nf,ne=mk_entry(ir,"e.g. Rice"); tk.Label(ir,text="Name",bg=C["surface"],fg=C["muted"],font=("Courier New",8)).pack(side="left"); nf.config(width=110); nf.pack(side="left",padx=(4,8))
            qf,qe=mk_entry(ir,"qty"); tk.Label(ir,text="Qty",bg=C["surface"],fg=C["muted"],font=("Courier New",8)).pack(side="left"); qf.config(width=55); qf.pack(side="left",padx=(4,8))
            ef,ee=mk_entry(ir,"hrs"); tk.Label(ir,text="Exp(h)",bg=C["surface"],fg=C["muted"],font=("Courier New",8)).pack(side="left"); ef.config(width=55); ef.pack(side="left",padx=(4,0))
            irows.append((ne,qe,ee))
        add_row(); add_row()
        tk.Button(inner,text=T("add_item"),bg=C["card"],fg=C["accent2"],font=("Courier New",9),
                 relief="flat",bd=0,cursor="hand2",command=add_row,pady=5).pack(anchor="w",pady=5)
        el=lbl(inner,"",size=10,color=C["error"]); el.pack(anchor="w")
        def submit():
            items=[]
            for ne,qe,ee in irows:
                n=ne.get().strip()
                if not n or n=="e.g. Rice": continue
                try: q=int(qe.get()); e=int(ee.get()); assert q>0 and e>0
                except: el.config(text="⚠  Enter valid numbers."); return
                items.append({"name":n,"qty":q,"expiry":e})
            if not items: el.config(text="⚠  Add at least one item."); return
            zone=zc.get(); summary="\n".join(f"  • {it["qty"]} meals of {it["name"]} (expires in {it["expiry"]}h)" for it in items)
            def do():
                did=self.db.add_donation(self.user["entity_id"],zone,items)
                self._toast(f"✅ Donation #{did} added!"); self._pg_my_don()
            confirm_dialog(self,T("confirm_title"),f"You are about to donate:\n{summary}\n\nZone: {zone}\n\nProceed?",do)
        mk_btn(inner,T("submit_donation"),submit,color=C["accent"],width=28).pack(pady=10)

    # ══════════════════════════════════════════
    #  MY REQUESTS  (Feature 4: hover)
    # ══════════════════════════════════════════
    def _pg_my_req(self):
        self._set_nav(T("my_requests")); self._on_dash=False
        eid=self.user["entity_id"]; my=[r for r in self.db.requests if r["receiver_id"]==eid]
        page=self._pg_frame(T("my_requests"),f"{len(my)} request(s) submitted")
        if not my: empty_state(page,"📋",T("no_requests"),"Use 'New Request' in the sidebar"); return
        uc={1:C["muted"],2:C["warning"],3:C["error"]}; ul={1:"LOW",2:"MEDIUM",3:"HIGH"}
        for req in my[::-1]:
            bc=uc.get(req["urgency"],C["border"])
            f=tk.Frame(page,bg=C["card"],highlightbackground=bc,highlightthickness=1); f.pack(fill="x",pady=5)
            f.bind("<Enter>",lambda e,fr=f: fr.config(highlightbackground=C["accent"],highlightthickness=2))
            f.bind("<Leave>",lambda e,fr=f,c=bc: fr.config(highlightbackground=c,highlightthickness=1))
            tk.Frame(f,bg=bc,height=3).pack(fill="x")
            inner=tk.Frame(f,bg=C["card"]); inner.pack(fill="x",padx=16,pady=12)
            hdr=tk.Frame(inner,bg=C["card"]); hdr.pack(fill="x")
            tk.Label(hdr,text="Request #"+str(req["id"]),bg=C["card"],fg=C["text"],font=("Courier New",12,"bold")).pack(side="left")
            tk.Label(hdr,text=" "+ul.get(req["urgency"],"?")+" ",bg=bc,fg=C["white"],font=("Courier New",8,"bold"),padx=5).pack(side="right")
            # Match status badge
            matched_r, donor_name, meals_r = self.db.is_request_matched(req["id"])
            sr=tk.Frame(inner,bg=C["card"]); sr.pack(fill="x",pady=(4,2))
            if matched_r:
                tk.Label(sr,text="✅ MATCHED",bg=C["success"],fg=C["white"],
                        font=("Courier New",8,"bold"),padx=8,pady=3).pack(side="left")
                tk.Label(sr,text=f"  ←  {donor_name}  •  {meals_r} meals allocated",
                        bg=C["card"],fg=C["success"],font=("Courier New",9,"bold")).pack(side="left")
            else:
                tk.Label(sr,text="⏳ PENDING",bg=C["warning"],fg=C["white"],
                        font=("Courier New",8,"bold"),padx=8,pady=3).pack(side="left")
                tk.Label(sr,text="  Waiting for a matching donation (same zone preferred)",
                        bg=C["card"],fg=C["muted"],font=("Courier New",9)).pack(side="left")
            tk.Label(inner,text="Item:"+req.get("item","Any")+"  •  Zone:"+req["zone"]+"  •  "+str(req["qty"])+" meals  •  "+req["timestamp"],
                    bg=C["card"],fg=C["muted"],font=("Courier New",9)).pack(anchor="w",pady=(2,0))

    # ══════════════════════════════════════════
    #  NEW REQUEST  (Feature 17: confirm)
    # ══════════════════════════════════════════
    def _pg_new_req(self):
        self._set_nav(T("new_request")); self._on_dash=False
        page=self._pg_frame(T("new_request"),"Request food for your organization")
        form=tk.Frame(page,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); form.pack(fill="x",pady=14)
        tk.Frame(form,bg=C["accent2"],height=4).pack(fill="x")
        inner=tk.Frame(form,bg=C["card"]); inner.pack(fill="x",padx=28,pady=20)
        lbl(inner,T("qty_needed"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(0,4))
        f1,qe=mk_entry(inner,"e.g. 50"); f1.pack(fill="x",pady=(0,10))
        lbl(inner,"FOOD ITEM",size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(0,4))
        fi,ie=mk_entry(inner,"e.g. Rice or Any"); fi.pack(fill="x",pady=(0,10))
        lbl(inner,T("zone_lbl"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(0,4))
        zc=mk_combo(inner,ZONES); zc.pack(anchor="w",pady=(0,10))
        lbl(inner,T("urgency"),size=9,color=C["muted"],bold=True).pack(anchor="w",pady=(0,6))
        uv=tk.IntVar(value=2)
        uf=tk.Frame(inner,bg=C["card"]); uf.pack(anchor="w",pady=(0,12))
        for v,t,col in [(1,"Low",C["muted"]),(2,"Medium",C["warning"]),(3,"High",C["error"])]:
            tk.Radiobutton(uf,text=t,variable=uv,value=v,bg=C["card"],fg=col,selectcolor=C["surface"],
                          activebackground=C["card"],font=("Courier New",11)).pack(side="left",padx=(0,20))
        el=lbl(inner,"",size=10,color=C["error"]); el.pack(anchor="w")
        def submit():
            try: qty=int(qe.get()); assert qty>0
            except: el.config(text="⚠  Enter a valid quantity."); return
            item=ie.get().strip() or "Any"
            zone=zc.get(); urgency=uv.get(); un={1:"Low",2:"Medium",3:"High"}.get(urgency,"")
            def do():
                rid=self.db.add_request(self.user["entity_id"],qty,urgency,zone,item)
                self._toast(f"✅ Request #{rid} submitted!",col=C["accent2"]); self._pg_my_req()
            confirm_dialog(self,T("confirm_title"),f"You are requesting:\n  • {qty} meals\n  • Item: {item}\n  • Zone: {zone}\n  • Urgency: {un}\n\nProceed?",do)
        mk_btn(inner,T("submit_request"),submit,color=C["accent2"],width=28).pack(pady=10)

    # ══════════════════════════════════════════
    #  ALL MEMBERS  (Donors + Receivers)
    # ══════════════════════════════════════════
    def _pg_all_members(self):
        self._set_nav("All Members"); self._on_dash=False
        stats=self.db.get_stats()
        page=self._pg_frame("👥 All Members",
            f"{stats['total_donors']} donors  •  {stats['total_receivers']} receivers  •  {stats['total_donations']} donations  •  {stats['total_requests']} requests")

        # ── TAB ROW ─────────────────────────────
        tab_var=tk.StringVar(value="donors")
        tab_f=tk.Frame(page,bg=C["bg"]); tab_f.pack(anchor="w",pady=(0,14))
        panels={}

        def show_tab(name):
            tab_var.set(name)
            for k,p in panels.items():
                if k==name: p.pack(fill="x")
                else: p.pack_forget()
            for k,b in tab_btns.items():
                if k==name: b.config(bg=C["accent"],fg=C["white"])
                else: b.config(bg=C["surface"],fg=C["muted"])

        tab_btns={}
        for name,label,count in [
            ("donors",  f"🟠 Donors ({stats['total_donors']})",   stats["total_donors"]),
            ("receivers",f"🔵 Receivers ({stats['total_receivers']})", stats["total_receivers"]),
        ]:
            b=tk.Button(tab_f,text=label,
                       bg=C["accent"] if name=="donors" else C["surface"],
                       fg=C["white"] if name=="donors" else C["muted"],
                       font=("Courier New",10,"bold"),relief="flat",bd=0,cursor="hand2",
                       padx=16,pady=8,command=lambda n=name:show_tab(n))
            b.pack(side="left",padx=(0,6)); tab_btns[name]=b

        # ── DONORS PANEL ────────────────────────
        donor_panel=tk.Frame(page,bg=C["bg"]); panels["donors"]=donor_panel

        # Summary stats row
        ds=tk.Frame(donor_panel,bg=C["bg"]); ds.pack(fill="x",pady=(0,12))
        lb_data=dict(self.db.get_leaderboard())
        total_donated=sum(self.db._qty(d) for d in self.db.donations)
        for i,(lbl_txt,val,col) in enumerate([
            ("Total Donors", len(self.db.donors), C["accent"]),
            ("Total Meals Donated", total_donated, C["success"]),
            ("Total Donations", len(self.db.donations), C["warning"]),
        ]):
            c=tk.Frame(ds,bg=C["card"],highlightbackground=col,highlightthickness=2); c.grid(row=0,column=i,padx=6,sticky="nsew"); ds.columnconfigure(i,weight=1)
            tk.Frame(c,bg=col,height=3).pack(fill="x")
            ci=tk.Frame(c,bg=C["card"]); ci.pack(fill="x",padx=14,pady=10)
            tk.Label(ci,text=lbl_txt,bg=C["card"],fg=C["muted"],font=("Courier New",8,"bold")).pack(anchor="w")
            tk.Label(ci,text=str(val),bg=C["card"],fg=C["text"],font=("Courier New",18,"bold")).pack(anchor="w")

        # Table header
        hdr=tk.Frame(donor_panel,bg=C["surface"],highlightbackground=C["border"],highlightthickness=1); hdr.pack(fill="x")
        for col,wid in [("ID",5),("Name",22),("Type",18),("Zone",10),("Contact",14),("Donations",10),("Meals Given",12),("Status",10)]:
            tk.Label(hdr,text=col,width=wid,bg=C["surface"],fg=C["muted"],
                    font=("Courier New",9,"bold"),anchor="w",padx=6,pady=8).pack(side="left")

        # Donor rows
        for uid,dn in self.db.donors.items():
            don_count=sum(1 for d in self.db.donations if d["donor_id"]==uid)
            meals_given=lb_data.get(dn["name"],0)
            is_active=any(d["donor_id"]==uid for d in self.db.donations)
            matched_count=sum(1 for m in self.db.matches if m["donor_name"]==dn["name"])

            row=tk.Frame(donor_panel,bg=C["white"],highlightbackground=C["border"],highlightthickness=1)
            row.pack(fill="x",pady=1)
            row.bind("<Enter>",lambda e,r=row:r.config(bg=_lt(C["accent"],0.9)))
            row.bind("<Leave>",lambda e,r=row:r.config(bg=C["white"]))

            vals=[
                (str(uid),5),(dn["name"][:20],22),(dn["type"],18),(dn["zone"],10),
                (dn["contact"],14),(str(don_count),10),(str(meals_given),12),
                ("✅ Active" if is_active else "○ None",10),
            ]
            for i,(txt,wid) in enumerate(vals):
                fg=C["success"] if "Active" in txt else C["muted"] if "None" in txt else C["text"]
                lbl_w=tk.Label(row,text=txt,width=wid,bg=C["white"],fg=fg,
                              font=("Courier New",9),anchor="w",padx=6,pady=8)
                lbl_w.pack(side="left")
                lbl_w.bind("<Enter>",lambda e,r=row:r.config(bg=_lt(C["accent"],0.9)))
                lbl_w.bind("<Leave>",lambda e,r=row:r.config(bg=C["white"]))

        if not self.db.donors:
            empty_state(donor_panel,"🟠","No donors registered yet.","Donors sign up from the registration page")

        # ── RECEIVERS PANEL ─────────────────────
        recv_panel=tk.Frame(page,bg=C["bg"]); panels["receivers"]=recv_panel

        rs=tk.Frame(recv_panel,bg=C["bg"]); rs.pack(fill="x",pady=(0,12))
        total_requested=sum(r["qty"] for r in self.db.requests)
        for i,(lbl_txt,val,col) in enumerate([
            ("Total Receivers", len(self.db.receivers), C["accent2"]),
            ("Total Meals Requested", total_requested, C["accent3"]),
            ("Total Requests", len(self.db.requests), C["warning"]),
        ]):
            c=tk.Frame(rs,bg=C["card"],highlightbackground=col,highlightthickness=2); c.grid(row=0,column=i,padx=6,sticky="nsew"); rs.columnconfigure(i,weight=1)
            tk.Frame(c,bg=col,height=3).pack(fill="x")
            ci=tk.Frame(c,bg=C["card"]); ci.pack(fill="x",padx=14,pady=10)
            tk.Label(ci,text=lbl_txt,bg=C["card"],fg=C["muted"],font=("Courier New",8,"bold")).pack(anchor="w")
            tk.Label(ci,text=str(val),bg=C["card"],fg=C["text"],font=("Courier New",18,"bold")).pack(anchor="w")

        hdr2=tk.Frame(recv_panel,bg=C["surface"],highlightbackground=C["border"],highlightthickness=1); hdr2.pack(fill="x")
        for col,wid in [("ID",5),("Name",22),("Type",14),("Zone",10),("Contact",14),("Urgency",10),("Requests",10),("Status",12)]:
            tk.Label(hdr2,text=col,width=wid,bg=C["surface"],fg=C["muted"],
                    font=("Courier New",9,"bold"),anchor="w",padx=6,pady=8).pack(side="left")

        urg_map={1:"Low",2:"Medium",3:"High"}
        urg_col={1:C["muted"],2:C["warning"],3:C["error"]}
        for uid,rn in self.db.receivers.items():
            req_count=sum(1 for r in self.db.requests if r["receiver_id"]==uid)
            is_matched=any(m["receiver_name"]==rn["name"] for m in self.db.matches)
            urg=rn.get("urgency",1)

            row=tk.Frame(recv_panel,bg=C["white"],highlightbackground=C["border"],highlightthickness=1)
            row.pack(fill="x",pady=1)
            row.bind("<Enter>",lambda e,r=row:r.config(bg=_lt(C["accent2"],0.9)))
            row.bind("<Leave>",lambda e,r=row:r.config(bg=C["white"]))

            vals=[
                (str(uid),5),(rn["name"][:20],22),(rn["type"],14),(rn["zone"],10),
                (rn["contact"],14),(urg_map.get(urg,"?"),10),(str(req_count),10),
                ("✅ Matched" if is_matched else "⏳ Waiting",12),
            ]
            for i,(txt,wid) in enumerate(vals):
                fg=C["success"] if "Matched" in txt else C["warning"] if "Waiting" in txt else urg_col.get(urg,C["muted"]) if i==5 else C["text"]
                lbl_w=tk.Label(row,text=txt,width=wid,bg=C["white"],fg=fg,
                              font=("Courier New",9),anchor="w",padx=6,pady=8)
                lbl_w.pack(side="left")
                lbl_w.bind("<Enter>",lambda e,r=row:r.config(bg=_lt(C["accent2"],0.9)))
                lbl_w.bind("<Leave>",lambda e,r=row:r.config(bg=C["white"]))

        if not self.db.receivers:
            empty_state(recv_panel,"🔵","No receivers registered yet.","Receivers sign up from the registration page")

        # Show donors tab by default
        show_tab("donors")

    # ══════════════════════════════════════════
    #  MATCHES
    # ══════════════════════════════════════════
    def _pg_matches(self):
        self._set_nav(T("matches")); self._on_dash=False
        page=self._pg_frame(T("matches"),f"{len(self.db.matches)} match(es) — {self.db.stats["total_meals"]} meals")
        br=tk.Frame(page,bg=C["bg"]); br.pack(anchor="e",pady=(0,8))
        def rerun(): self.db._run_matching(); self.db._log("SYSTEM","Re-run manually"); self._pg_matches()
        mk_btn(br,"🔄 "+T("rerun"),rerun,color=C["accent2"],width=20,fs=10).pack(side="right")
        if not self.db.matches: empty_state(page,"🔗",T("no_matches"),"Matching runs automatically when zones align"); return
        hdr=tk.Frame(page,bg=C["surface"],highlightbackground=C["border"],highlightthickness=1); hdr.pack(fill="x")
        for ct,wid in [("#D",4),("#R",4),("Donor",16),("Receiver",16),("Item",12),("Zone",7),("Meals",6),("Type",8),("Urgency",8),("Reason",20)]:
            tk.Label(hdr,text=ct,width=wid,bg=C["surface"],fg=C["muted"],font=("Courier New",9,"bold"),anchor="w",padx=4,pady=8).pack(side="left")
        uc={1:C["muted"],2:C["warning"],3:C["error"]}; ul={1:"Low",2:"Med",3:"High"}
        for m in self.db.matches:
            row=tk.Frame(page,bg=C["white"],highlightbackground=C["border"],highlightthickness=1); row.pack(fill="x",pady=1)
            pt="⚖Partial" if m.get("partial") else "✅Full"; ptc=C["warning"] if m.get("partial") else C["success"]
            vals=[(str(m["donation_id"]),4),(str(m["request_id"]),4),(m["donor_name"][:14],16),(m["receiver_name"][:14],16),
                  (m.get("item","Any")[:10],12),(m["zone"],7),(str(m["meals"]),6),(pt,8),(ul.get(m.get("urgency",1),"?"),8),(m.get("reason","")[:20],20)]
            for i,(txt,wid) in enumerate(vals):
                fg=uc.get(m.get("urgency",1),C["muted"]) if i==8 else ptc if i==7 else C["text"]
                tk.Label(row,text=txt,width=wid,bg=C["white"],fg=fg,font=("Courier New",9),anchor="w",padx=4,pady=7).pack(side="left")

    # ══════════════════════════════════════════
    #  SMART MATCH
    # ══════════════════════════════════════════
    def _pg_smart(self):
        self._set_nav(T("smart_match")); self._on_dash=False
        page=self._pg_frame("🧠 "+T("smart_match"),"Scored pairs ranked by expiry urgency and receiver need")
        sug=self.db.get_smart()
        if not sug: empty_state(page,"🎉","All eligible donations matched!","Great work — system fully utilized"); return
        for i,s in enumerate(sug):
            don=s["don"]; req=s["req"]
            dn=self.db.donors.get(don["donor_id"],{}).get("name","?")
            rn=self.db.receivers.get(req["receiver_id"],{}).get("name","?")
            border=C["accent"] if i==0 else C["border"]
            card=tk.Frame(page,bg=C["card"],highlightbackground=border,highlightthickness=1); card.pack(fill="x",pady=6)
            tk.Frame(card,bg=border,height=4).pack(fill="x")
            inner=tk.Frame(card,bg=C["white"]); inner.pack(fill="x",padx=20,pady=14)
            hrow=tk.Frame(inner,bg=C["white"]); hrow.pack(fill="x")
            tk.Label(hrow,text=["🥇 Best Match","🥈 Second","🥉 Third"][i],bg=C["white"],fg=border,font=("Courier New",12,"bold")).pack(side="left")
            tk.Label(hrow,text=f"Score: {s["score"]}",bg=C["white"],fg=C["muted"],font=("Courier New",10)).pack(side="right")
            exp=self.db._expiry(don); ecol=C["urgent"] if exp<=2 else C["warning"] if exp<=5 else C["muted"]
            tk.Label(inner,text=f"Donor: {dn} ({don["zone"]})",bg=C["white"],fg=C["text"],font=("Courier New",11)).pack(anchor="w",pady=(8,2))
            tk.Label(inner,text=f"Receiver: {rn}  |  Item:{req.get('item','Any')}  |  Urgency:{req["urgency"]}  |  Needs:{req["qty"]} meals",bg=C["white"],fg=C["text"],font=("Courier New",11)).pack(anchor="w",pady=(0,2))
            tk.Label(inner,text=f"Expiry: {exp}h  •  "+", ".join(f"{it["name"]}({it["qty"]})" for it in don["items"]),bg=C["white"],fg=ecol,font=("Courier New",9)).pack(anchor="w",pady=(0,6))
            tk.Label(inner,text=f"💡 {s["reason"]}",bg=C["white"],fg=C["accent2"],font=("Courier New",9,"bold")).pack(anchor="w")

    # ══════════════════════════════════════════
    #  ZONE MAP  (Feature 9: click popup)
    # ══════════════════════════════════════════
    def _pg_zone(self):
        self._set_nav(T("zone_map")); self._on_dash=False
        zm=self.db.get_zone_map()
        page=self._pg_frame("🗺 "+T("zone_map"),"Click any zone for details — green=surplus, red=deficit")
        mc=tk.Frame(page,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); mc.pack(fill="x",pady=(8,14))
        cv=tk.Canvas(mc,width=840,height=300,bg=C["card"],highlightthickness=0,bd=0); cv.pack(padx=10,pady=12)
        self._draw_zone_cv(cv,zm,840,300)
        g=tk.Frame(page,bg=C["bg"]); g.pack(fill="x")
        for i,z in enumerate(ZONES):
            d=zm.get(z,{}); su=d.get("surplus",0); de=d.get("demand",0)
            st="SURPLUS" if su>de else "DEFICIT" if de>su else "BALANCED"
            sc=C["success"] if st=="SURPLUS" else C["error"] if st=="DEFICIT" else C["warning"]
            zc=tk.Frame(g,bg=C["card"],highlightbackground=sc,highlightthickness=1); zc.grid(row=0,column=i,padx=6,sticky="nsew"); g.columnconfigure(i,weight=1)
            tk.Frame(zc,bg=sc,height=4).pack(fill="x")
            zi=tk.Frame(zc,bg=C["card"]); zi.pack(fill="x",padx=14,pady=12)
            tk.Label(zi,text=z,bg=C["card"],fg=C["text"],font=("Courier New",13,"bold")).pack(anchor="w")
            tk.Label(zi,text=st,bg=C["card"],fg=sc,font=("Courier New",9,"bold")).pack(anchor="w",pady=(2,6))
            for k2,v2,c2 in [("Surplus",f"{su}m",C["accent"]),("Demand",f"{de}m",C["accent3"]),("Donations",d.get("donations",0),C["muted"]),("Requests",d.get("requests",0),C["muted"])]:
                r=tk.Frame(zi,bg=C["card"]); r.pack(fill="x",pady=1)
                tk.Label(r,text=k2+":",bg=C["card"],fg=C["muted"],font=("Courier New",9),width=10,anchor="w").pack(side="left")
                tk.Label(r,text=str(v2),bg=C["card"],fg=c2,font=("Courier New",9,"bold")).pack(side="left")

    def _draw_zone_cv(self,cv,zm,w,h):
        pos={"Zone A":(0,0),"Zone B":(1,0),"Zone C":(0,1),"Zone D":(1,1)}
        cw=(w-50)//2; ch=(h-30)//2
        for z,(col,row) in pos.items():
            d=zm.get(z,{}); su=d.get("surplus",0); de=d.get("demand",0)
            x0=20+col*(cw+10); y0=8+row*(ch+8); x1=x0+cw; y1=y0+ch
            fill=_lt(C["success"],0.6) if su>de else _lt(C["error"],0.5) if de>su else C["surface"]
            cv.create_rectangle(x0,y0,x1,y1,fill=fill,outline=C["accent"],width=2,tags=f"z_{z}")
            st="SURPLUS" if su>de else "DEFICIT" if de>su else "BALANCED"
            sc=C["success"] if st=="SURPLUS" else C["error"] if st=="DEFICIT" else C["warning"]
            cv.create_text((x0+x1)//2,(y0+y1)//2-18,text=z,fill=C["text"],font=("Courier New",13,"bold"),tags=f"z_{z}")
            cv.create_text((x0+x1)//2,(y0+y1)//2+2,text=st,fill=sc,font=("Courier New",10,"bold"),tags=f"z_{z}")
            cv.create_text((x0+x1)//2,(y0+y1)//2+20,text=f"S:{su}  D:{de}",fill=C["muted"],font=("Courier New",9),tags=f"z_{z}")
            cv.tag_bind(f"z_{z}","<Button-1>",lambda e,zn=z,zm2=zm: self._zone_pop(zn,zm2))
            cv.tag_bind(f"z_{z}","<Enter>",lambda e: cv.config(cursor="hand2"))
            cv.tag_bind(f"z_{z}","<Leave>",lambda e: cv.config(cursor=""))

    def _zone_pop(self,zone,zm):
        d=zm.get(zone,{}); su=d.get("surplus",0); de=d.get("demand",0)
        dlg=tk.Toplevel(self); dlg.title(zone); dlg.configure(bg=C["bg"]); dlg.resizable(False,False); dlg.grab_set()
        w,h=360,290; sw=self.winfo_screenwidth(); sh=self.winfo_screenheight()
        dlg.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")
        tk.Frame(dlg,bg=C["accent"],height=4).pack(fill="x")
        body=tk.Frame(dlg,bg=C["bg"]); body.pack(fill="both",expand=True,padx=24,pady=18)
        st="SURPLUS" if su>de else "DEFICIT" if de>su else "BALANCED"
        sc=C["success"] if st=="SURPLUS" else C["error"] if st=="DEFICIT" else C["warning"]
        tk.Label(body,text=f"🗺 {zone}",bg=C["bg"],fg=C["accent"],font=("Courier New",18,"bold")).pack(anchor="w")
        tk.Label(body,text=f"Status: {st}",bg=C["bg"],fg=sc,font=("Courier New",12,"bold")).pack(anchor="w",pady=(4,10))
        for k,v,col in [("Surplus (meals)",su,C["accent"]),("Demand (meals)",de,C["accent3"]),("Donations",d.get("donations",0),C["warning"]),("Requests",d.get("requests",0),C["muted"])]:
            r=tk.Frame(body,bg=C["bg"]); r.pack(fill="x",pady=4)
            tk.Label(r,text=k+":",bg=C["bg"],fg=C["muted"],font=("Courier New",10),width=20,anchor="w").pack(side="left")
            tk.Label(r,text=str(v),bg=C["bg"],fg=col,font=("Courier New",13,"bold")).pack(side="left")
        mk_btn(body,"Close",dlg.destroy,color=C["surface"],width=10,fg=C["muted"],fs=10).pack(pady=(14,0))

    # ══════════════════════════════════════════
    #  CALENDAR  (Feature 8)
    # ══════════════════════════════════════════
    def _pg_cal(self):
        self._set_nav(T("calendar")); self._on_dash=False
        now=datetime.now(); self._cy=now.year; self._cm=now.month
        for w in self._content.winfo_children(): w.destroy()
        sf=SF(self._content); sf.pack(fill="both",expand=True)
        self._cal_p=sf.inner; self._cal_p.config(bg=C["bg"],padx=30,pady=22)
        lbl(self._cal_p,"📅 "+T("calendar"),size=20,bold=True).pack(anchor="w")
        lbl(self._cal_p,"Darker orange = more meals donated that day",size=10,color=C["muted"]).pack(anchor="w",pady=(2,12))
        sep_line(self._cal_p)
        self._cal_body=tk.Frame(self._cal_p,bg=C["bg"]); self._cal_body.pack(fill="x")
        self._render_cal()

    def _render_cal(self):
        for w in self._cal_body.winfo_children(): w.destroy()
        nav=tk.Frame(self._cal_body,bg=C["bg"]); nav.pack(fill="x",pady=(0,10))
        def prev():
            self._cm-=1
            if self._cm<1: self._cm=12; self._cy-=1
            self._render_cal()
        def nxt():
            self._cm+=1
            if self._cm>12: self._cm=1; self._cy+=1
            self._render_cal()
        mk_btn(nav,"◀",prev,color=C["surface"],fg=C["text"],width=3,fs=11).pack(side="left")
        tk.Label(nav,text=datetime(self._cy,self._cm,1).strftime("%B %Y"),bg=C["bg"],fg=C["text"],font=("Courier New",14,"bold")).pack(side="left",padx=20)
        mk_btn(nav,"▶",nxt,color=C["surface"],fg=C["text"],width=3,fs=11).pack(side="left")
        cal_data=self.db.get_cal(self._cy,self._cm); mx=max(cal_data.values()) if cal_data else 1
        cf=tk.Frame(self._cal_body,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); cf.pack(fill="x",pady=4)
        for i,d in enumerate(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]):
            tk.Label(cf,text=d,bg=C["surface"],fg=C["muted"],font=("Courier New",9,"bold"),width=9,pady=6).grid(row=0,column=i,sticky="nsew",padx=1,pady=1)
        today=datetime.now()
        for wi,week in enumerate(calendar.monthcalendar(self._cy,self._cm)):
            for di,day in enumerate(week):
                r=wi+1; c=di
                if day==0: tk.Label(cf,text="",bg=C["bg"],width=9,height=4).grid(row=r,column=c,sticky="nsew",padx=1,pady=1); continue
                meals=cal_data.get(day,0); intensity=meals/mx if mx>0 else 0
                bg_col=_lt(C["accent"],1-intensity*0.7) if meals>0 else C["card"]
                is_today=(day==today.day and self._cm==today.month and self._cy==today.year)
                cell=tk.Frame(cf,bg=bg_col,highlightbackground=C["accent"] if is_today else C["border"],highlightthickness=2 if is_today else 1,width=90,height=64)
                cell.grid(row=r,column=c,sticky="nsew",padx=1,pady=1); cell.pack_propagate(False)
                tk.Label(cell,text=str(day),bg=bg_col,fg=C["accent"] if is_today else C["text"],font=("Courier New",10,"bold" if is_today else "normal")).pack(anchor="nw",padx=4,pady=2)
                if meals>0: tk.Label(cell,text=f"{meals}m",bg=bg_col,fg=C["white"] if intensity>0.5 else C["accent"],font=("Courier New",8,"bold")).pack(anchor="s",pady=2)
                cf.columnconfigure(c,weight=1)

    # ══════════════════════════════════════════
    #  ALL MEMBERS (Donors + Receivers)
    # ══════════════════════════════════════════
    def _pg_all_members(self):
        self._set_nav("All Members"); self._on_dash=False
        page=self._pg_frame("👥 All Members",
            f"{len(self.db.donors)} donor(s)  •  {len(self.db.receivers)} receiver(s) registered")

        # ── Donors section ──
        don_hdr=tk.Frame(page,bg=C["surface"],highlightbackground=C["border"],highlightthickness=1)
        don_hdr.pack(fill="x",pady=(8,0))
        tk.Label(don_hdr,text="🟠  FOOD DONORS",bg=C["surface"],fg=C["accent"],
                font=("Courier New",12,"bold")).pack(side="left",padx=14,pady=10)
        tk.Label(don_hdr,text=str(len(self.db.donors))+" registered",bg=C["surface"],
                fg=C["muted"],font=("Courier New",10)).pack(side="right",padx=14)

        if not self.db.donors:
            empty_state(page,"🏷","No donors yet.","Register a donor account to get started")
        else:
            # Table header
            th=tk.Frame(page,bg=C["border"]); th.pack(fill="x")
            for col_txt,wid in [("ID",5),("Name",22),("Type",16),("Zone",10),
                                 ("Contact",14),("Donations",10),("Meals Given",12)]:
                tk.Label(th,text=col_txt,width=wid,bg=C["surface"],fg=C["muted"],
                        font=("Courier New",9,"bold"),anchor="w",padx=6,pady=7).pack(side="left")

            for uid,dn in sorted(self.db.donors.items()):
                # Count donations & meals for this donor
                don_count=sum(1 for d in self.db.donations if d["donor_id"]==uid)
                meals_given=sum(m["meals"] for m in self.db.matches if m["donor_name"]==dn["name"])

                row=tk.Frame(page,bg=C["white"],highlightbackground=C["border"],highlightthickness=1)
                row.pack(fill="x",pady=1)
                # Hover
                row.bind("<Enter>",lambda e,r=row:r.config(bg=C["surface"]))
                row.bind("<Leave>",lambda e,r=row:r.config(bg=C["white"]))

                vals=[(str(uid),5),(dn["name"][:20],22),(dn.get("type",""),16),
                      (dn["zone"],10),(dn["contact"],14),(str(don_count),10),(str(meals_given),12)]
                for txt,wid in vals:
                    tk.Label(row,text=txt,width=wid,bg=C["white"],fg=C["text"],
                            font=("Courier New",10),anchor="w",padx=6,pady=8).pack(side="left")
                # meals given colored
                if meals_given>0:
                    row.winfo_children()[-1].config(fg=C["success"],font=("Courier New",10,"bold"))

        # ── Receivers section ──
        sep_line(page,pady=14)
        rec_hdr=tk.Frame(page,bg=C["surface"],highlightbackground=C["border"],highlightthickness=1)
        rec_hdr.pack(fill="x",pady=(0,0))
        tk.Label(rec_hdr,text="🔵  FOOD RECEIVERS",bg=C["surface"],fg=C["accent2"],
                font=("Courier New",12,"bold")).pack(side="left",padx=14,pady=10)
        tk.Label(rec_hdr,text=str(len(self.db.receivers))+" registered",bg=C["surface"],
                fg=C["muted"],font=("Courier New",10)).pack(side="right",padx=14)

        if not self.db.receivers:
            empty_state(page,"🤝","No receivers yet.","Register a receiver account to get started")
        else:
            th2=tk.Frame(page,bg=C["border"]); th2.pack(fill="x")
            for col_txt,wid in [("ID",5),("Name",22),("Type",14),("Zone",10),
                                 ("Contact",14),("Urgency",10),("Requests",10),("Meals Got",12)]:
                tk.Label(th2,text=col_txt,width=wid,bg=C["surface"],fg=C["muted"],
                        font=("Courier New",9,"bold"),anchor="w",padx=6,pady=7).pack(side="left")

            urg_colors={1:C["muted"],2:C["warning"],3:C["error"]}
            urg_labels={1:"Low",2:"Medium",3:"High"}
            for uid,rn in sorted(self.db.receivers.items()):
                req_count=sum(1 for r in self.db.requests if r["receiver_id"]==uid)
                meals_got=sum(m["meals"] for m in self.db.matches if m["receiver_name"]==rn["name"])
                urg=rn.get("urgency",1)

                row=tk.Frame(page,bg=C["white"],highlightbackground=C["border"],highlightthickness=1)
                row.pack(fill="x",pady=1)
                row.bind("<Enter>",lambda e,r=row:r.config(bg=C["surface"]))
                row.bind("<Leave>",lambda e,r=row:r.config(bg=C["white"]))

                for txt,wid in [(str(uid),5),(rn["name"][:20],22),(rn.get("type",""),14),
                                (rn["zone"],10),(rn["contact"],14),(urg_labels.get(urg,"?"),10),
                                (str(req_count),10),(str(meals_got),12)]:
                    tk.Label(row,text=txt,width=wid,bg=C["white"],fg=C["text"],
                            font=("Courier New",10),anchor="w",padx=6,pady=8).pack(side="left")
                # Color urgency cell
                urg_lbl=row.winfo_children()[5]
                urg_lbl.config(fg=urg_colors.get(urg,C["muted"]),font=("Courier New",10,"bold"))
                if meals_got>0:
                    row.winfo_children()[-1].config(fg=C["accent2"],font=("Courier New",10,"bold"))

    # ══════════════════════════════════════════
    #  LEADERBOARD
    # ══════════════════════════════════════════
    def _pg_lb(self):
        self._set_nav(T("leaderboard")); self._on_dash=False
        page=self._pg_frame("🏆 "+T("leaderboard"),"Top donors ranked by meals contributed")
        lb=self.db.get_leaderboard()
        if not lb: empty_state(page,"🏆",T("no_data"),"Start donating to appear here"); return
        medals=["🥇","🥈","🥉"]; mx=lb[0][1] if lb else 1
        for i,(name,meals) in enumerate(lb):
            f=tk.Frame(page,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); f.pack(fill="x",pady=4)
            inner=tk.Frame(f,bg=C["card"]); inner.pack(fill="x",padx=16,pady=12)
            top=tk.Frame(inner,bg=C["card"]); top.pack(fill="x")
            medal=medals[i] if i<3 else f"#{i+1}"
            tk.Label(top,text=f"{medal}  {name}",bg=C["card"],fg=C["text"],font=("Courier New",12,"bold" if i<3 else "normal")).pack(side="left")
            tk.Label(top,text=f"{meals} meals  •  {round(meals*KG_PER_MEAL,1)} kg saved",bg=C["card"],fg=C["accent"],font=("Courier New",10,"bold")).pack(side="right")
            bar_f=tk.Frame(inner,bg=C["border"],height=8); bar_f.pack(fill="x",pady=(6,0))
            bc=[C["accent"],C["warning"],C["accent2"]][min(i,2)]
            tk.Frame(bar_f,bg=bc,height=8,width=int((meals/mx)*680)).place(x=0,y=0)

    # ══════════════════════════════════════════
    #  HISTORY
    # ══════════════════════════════════════════
    def _pg_hist(self):
        self._set_nav(T("history")); self._on_dash=False
        page=self._pg_frame("📜 "+T("history"),f"{len(self.db.history)} event(s) recorded")
        fb=tk.Frame(page,bg=C["bg"]); fb.pack(anchor="w",pady=(0,10))
        lbl(fb,"Filter:",size=10,color=C["muted"]).pack(side="left",padx=(0,8))
        fv=tk.StringVar(value="ALL"); log_f=tk.Frame(page,bg=C["bg"]); log_f.pack(fill="x")
        for fval in ["ALL","DONATION","REQUEST","MATCH","REGISTER","LOGIN","SYSTEM"]:
            tk.Radiobutton(fb,text=fval,variable=fv,value=fval,bg=C["bg"],fg=C["muted"],
                          selectcolor=C["surface"],activebackground=C["bg"],font=("Courier New",8),
                          command=lambda: self._ref_hist(log_f,fv.get())).pack(side="left",padx=4)
        self._ref_hist(log_f,"ALL")

    def _ref_hist(self,log_f,fval):
        for w in log_f.winfo_children(): w.destroy()
        tc={"DONATION":C["accent"],"REQUEST":C["accent2"],"MATCH":C["success"],"REGISTER":C["warning"],"LOGIN":C["muted"],"SYSTEM":C["accent3"]}
        events=[e for e in self.db.history[::-1] if fval=="ALL" or e["type"]==fval]
        if not events: empty_state(log_f,"📜","No events found.","Try a different filter"); return
        for e in events[:100]:
            row=tk.Frame(log_f,bg=C["white"],highlightbackground=C["border"],highlightthickness=1); row.pack(fill="x",pady=2)
            inner=tk.Frame(row,bg=C["white"]); inner.pack(fill="x",padx=12,pady=7)
            col=tc.get(e["type"],C["muted"])
            tk.Label(inner,text=f" {e["type"]} ",bg=col,fg=C["white"],font=("Courier New",8,"bold"),padx=4).pack(side="left",padx=(0,10))
            tk.Label(inner,text=e["time"],bg=C["white"],fg=C["muted"],font=("Courier New",9)).pack(side="left",padx=(0,12))
            tk.Label(inner,text=e["msg"],bg=C["white"],fg=C["text"],font=("Courier New",10)).pack(side="left")

    # ══════════════════════════════════════════
    #  STATISTICS  (Feature 10: progress rings, Feature 13: PDF)
    # ══════════════════════════════════════════
    def _pg_stats(self):
        self._set_nav(T("statistics")); self._on_dash=False
        page=self._pg_frame(T("statistics"),"System-wide performance overview")
        stats=self.db.get_stats(); waste=self.db.get_waste()
        # KPI
        g=tk.Frame(page,bg=C["bg"]); g.pack(fill="x",pady=(6,12))
        kpis=[(T("total_donors"),stats["total_donors"],C["accent"],"🏷"),(T("total_receivers"),stats["total_receivers"],C["accent2"],"🤝"),
              ("Donations",stats["total_donations"],C["warning"],"📦"),("Requests",stats["total_requests"],C["accent3"],"📋"),
              (T("active_matches"),stats["total_matches"],C["success"],"🔗"),(T("meals_saved"),stats["total_meals"],C["success"],"🍽")]
        for i,(lb2,v,col,ic) in enumerate(kpis):
            stat_card(g,lb2,v,col,ic).grid(row=0,column=i,padx=4,sticky="nsew"); g.columnconfigure(i,weight=1)
        # Waste
        wf=tk.Frame(page,bg=C["card"],highlightbackground=C["accent3"],highlightthickness=1); wf.pack(fill="x",pady=(0,12))
        tk.Frame(wf,bg=C["accent3"],height=4).pack(fill="x")
        wi=tk.Frame(wf,bg=C["card"]); wi.pack(fill="x",padx=20,pady=12)
        tk.Label(wi,text="♻  Waste Prevention Impact",bg=C["card"],fg=C["text"],font=("Courier New",12,"bold")).pack(anchor="w",pady=(0,8))
        wg=tk.Frame(wi,bg=C["card"]); wg.pack(fill="x")
        for j,(wl,wv,wc) in enumerate([("Food Waste Prevented",f"{waste["kg"]} kg",C["success"]),("CO₂ Saved",f"{waste["co2"]} kg",C["accent2"]),("Meals Redistributed",str(waste["meals"]),C["warning"])]):
            wcc=tk.Frame(wg,bg=C["bg"],highlightbackground=wc,highlightthickness=1); wcc.grid(row=0,column=j,padx=6,sticky="nsew"); wg.columnconfigure(j,weight=1)
            tk.Frame(wcc,bg=wc,height=3).pack(fill="x")
            tk.Label(wcc,text=wl,bg=C["bg"],fg=C["muted"],font=("Courier New",8,"bold"),pady=4).pack()
            tk.Label(wcc,text=wv,bg=C["bg"],fg=wc,font=("Courier New",15,"bold")).pack()
        sep_line(page)
        # Charts
        cr=tk.Frame(page,bg=C["bg"]); cr.pack(fill="x",pady=6)
        bc2=tk.Frame(cr,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); bc2.grid(row=0,column=0,padx=(0,6),sticky="nsew")
        tk.Label(bc2,text="Meals by Zone",bg=C["card"],fg=C["text"],font=("Courier New",11,"bold")).pack(anchor="w",padx=12,pady=(10,4))
        cv1=tk.Canvas(bc2,width=290,height=175,bg=C["card"],highlightthickness=0,bd=0); cv1.pack(padx=8,pady=(0,10))
        draw_bar(cv1,stats["zone_dist"],w=290,h=175)
        dc=tk.Frame(cr,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); dc.grid(row=0,column=1,padx=(0,6),sticky="nsew")
        tk.Label(dc,text="Requests by Urgency",bg=C["card"],fg=C["text"],font=("Courier New",11,"bold")).pack(anchor="w",padx=12,pady=(10,4))
        cv2=tk.Canvas(dc,width=185,height=185,bg=C["card"],highlightthickness=0,bd=0); cv2.pack(padx=8,pady=(0,10))
        draw_donut(cv2,{"Low":stats["urgency_counts"].get(1,0),"Med":stats["urgency_counts"].get(2,0),"High":stats["urgency_counts"].get(3,0)},colors=[C["muted"],C["warning"],C["error"]],w=185,h=185)
        tc=tk.Frame(cr,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); tc.grid(row=0,column=2,sticky="nsew")
        tk.Label(tc,text="7-Day Trend",bg=C["card"],fg=C["text"],font=("Courier New",11,"bold")).pack(anchor="w",padx=12,pady=(10,4))
        cv3=tk.Canvas(tc,width=255,height=185,bg=C["card"],highlightthickness=0,bd=0); cv3.pack(padx=8,pady=(0,10))
        draw_line(cv3,self.db.get_trend(),w=255,h=185)
        cr.columnconfigure(0,weight=2); cr.columnconfigure(1,weight=1); cr.columnconfigure(2,weight=2)
        sep_line(page)
        # Feature 10: Progress rings + Feature 13: Export
        bot=tk.Frame(page,bg=C["bg"]); bot.pack(fill="x",pady=8)
        pr=tk.Frame(bot,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); pr.grid(row=0,column=0,padx=(0,8),sticky="nsew")
        tk.Frame(pr,bg=C["success"],height=4).pack(fill="x")
        pri=tk.Frame(pr,bg=C["card"]); pri.pack(fill="x",padx=18,pady=12)
        tk.Label(pri,text="📊 Match Efficiency Rings",bg=C["card"],fg=C["text"],font=("Courier New",12,"bold")).pack(anchor="w",pady=(0,10))
        rr=tk.Frame(pri,bg=C["card"]); rr.pack(anchor="w")
        td=stats["total_donations"]; tr=stats["total_requests"]; tm=stats["total_matches"]
        for rv,rm,rc,rl in [(tm,max(td,1),C["accent"],"Donation\nRate"),(tm,max(tr,1),C["accent2"],"Request\nRate"),(stats["total_meals"],max(tm*50,1),C["success"],"Meal\nRate")]:
            rcc=tk.Canvas(rr,width=110,height=110,bg=C["card"],highlightthickness=0,bd=0); rcc.pack(side="left",padx=6)
            draw_ring(rcc,rv,rm,rc,110,110,rl)
        xf=tk.Frame(bot,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); xf.grid(row=0,column=1,sticky="nsew")
        tk.Frame(xf,bg=C["accent2"],height=4).pack(fill="x")
        xi=tk.Frame(xf,bg=C["white"]); xi.pack(fill="x",padx=18,pady=12)
        tk.Label(xi,text="📄 Export & Reports",bg=C["white"],fg=C["text"],font=("Courier New",12,"bold")).pack(anchor="w",pady=(0,8))
        def ex_csv():
            p=filedialog.asksaveasfilename(defaultextension=".csv",filetypes=[("CSV","*.csv")],initialfile="mealbridge.csv")
            if p: self.db.export_csv(p); self._toast("✅ CSV exported!")
        def ex_json():
            p=filedialog.asksaveasfilename(defaultextension=".json",filetypes=[("JSON","*.json")],initialfile="mealbridge.json")
            if p: self.db.export_json(p); self._toast("✅ JSON exported!")
        def ex_rpt():
            p=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text","*.txt")],initialfile="mealbridge_report.txt")
            if p: ok=self.db.export_report(p); self._toast("✅ Report saved!" if ok else "❌ Failed",col=C["success"] if ok else C["error"])
        for txt,cmd,col in [(T("export_csv"),ex_csv,C["accent"]),(T("export_json"),ex_json,C["accent2"]),("📄 Print Report (.txt)",ex_rpt,C["accent3"])]:
            mk_btn(xi,txt,cmd,color=col,width=24,fs=10).pack(fill="x",pady=3)
        sep_line(xi,pady=8)
        tk.Label(xi,text="Keyboard Shortcuts:\nCtrl+D → Add Donation\nCtrl+R → New Request\nCtrl+M → Matches\nCtrl+S → Statistics\nCtrl+L → Logout",
                bg=C["white"],fg=C["muted"],font=("Courier New",8),justify="left").pack(anchor="w")
        bot.columnconfigure(0,weight=2); bot.columnconfigure(1,weight=1)

if __name__=="__main__":
    app=App(); app.mainloop()
