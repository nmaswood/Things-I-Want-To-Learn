import re
s = """
WASHINGTON — President-elect Donald J. Trump on Sunday chose Reince Priebus, the chairman of the Republican National Committee and a loyal campaign adviser, to be his White House chief of staff, turning to a Washington insider whose friendship with the House speaker, Paul D. Ryan, could help secure early legislative victories.

In selecting Mr. Priebus, the president-elect passed over Stephen K. Bannon, the right-wing media mogul who oversaw his presidential campaign. If Mr. Trump had appointed Mr. Bannon, a fierce critic of the Republican establishment, it would have signaled a continued disdain for a party that Mr. Trump fought throughout his campaign.

Mr. Trump’s choice is certain to anger some of his most conservative supporters, many of whom expect him to battle the Washington establishment over issues like taxes, immigration, trade, health care and the environment. They view Mr. Priebus as a deal maker who will be too eager to push the new president toward compromise.

In a statement Sunday afternoon, the transition team said Mr. Bannon would serve as the chief strategist and senior counselor in the White House. It emphasized that the two men would work “as equal partners to transform the federal government.”

Mr. Bannon — the longtime chairman of Breitbart News, a site known for its nationalist, racially charged, conspiracy-laden coverage — is likely to serve as a conduit to the populist right and conservative media outlets.

The transition team appeared eager to ease concerns among Mr. Trump’s most fervent supporters over the selection of Mr. Priebus. To that end, the statement mentioned Mr. Bannon first.

“We had a very successful partnership on the campaign, one that led to victory,” Mr. Bannon said in the statement. “We will have that same partnership in working to help President-elect Trump achieve his agenda.”

Mr. Priebus said he looked forward to working with Mr. Bannon and Mr. Trump “to create an economy that works for everyone, secure our borders, repeal and replace Obamacare and destroy radical Islamic terrorism.”

The selection of Mr. Priebus to run the White House staff is partly a reflection of concern among Mr. Trump’s children, especially Ivanka Trump, as well as her husband, Jared Kushner, that the job should not be held by someone too controversial, according to several people familiar with the internal decision making.

But while Mr. Trump apparently feels comfortable with Mr. Priebus, the people with knowledge of the decision said that Mr. Bannon was better able to talk forcefully to the president-elect during difficult moments.

Mr. Priebus is expected to have multiple deputies, including Katie Walsh, the chief of staff of the Republican National Committee, who is close to Mr. Priebus and helped ensure a tight working relationship between the party’s operational infrastructure and Mr. Trump’s campaign.
June 24, August 9, Dec 12
"""

#matchList = re.findall(r'([a-zA-z]+) (\d+[,\s])', s)
#regex = r"([a-zA-Z]+) (\d+)"
#res = re.sub(regex, r"\2 of \1", s)
#print(res)

line  = 'Cats are not smarter than dogs'

obj = re.findall(r"(\w+) feels (\w+) .*", s, re.M| re.I)

p = '860-834-6298'
#p = '.,,,,sdf,,,.sdf'

num = re.split('[,.;\- ]', p)

#obj= re.findall(r"(\d+)[- ](\d+)[- ](\d+)", p)
obj = re.findall(r'\A[T|t]he[\s]', s)

print (obj)










