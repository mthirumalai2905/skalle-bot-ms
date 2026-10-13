# About Synx and the Cioty hello-world tutorials

Tutorials for the Cioty trial of Synx HIVE. domain.cioty.com is a maker space run by Nornir, not a description of a Morph Space screen. synxpass.com is where this tutorial says you register. Do not paste a sample token. The person uses their own.

## Synx BIOS in short

Synx BIOS was designed for real-time transport, extreme scalability, data decoupling, event-driven distribution, and interoperability, while staying backwards compatible with World Wide Web linking. Standard web technology for the applications. The management of physical things is the part that differs.

## Hello World service

Register at synxpass.com, then request a domain at domain.cioty.com. This tutorial says the trial is free.

Create a morphic service:

- Name: HelloWorld
- Schema:

```xml
<rtw>
<txt></txt>
</rtw>
```

- Command schema empty
- Connection timeout 120 seconds
- Num ghosts: 5

Micropage title: This is a hello world demo. Description: a simple demo sending "Hello World". Picture URL blank. The public page is http://YourDomainName.cioty.com/helloworld

Listen, Synx-Cat 4, objectID 1. Send, Synx-Cat 1, objectID 3, field txt set to Hello World. Replace the domain and use your own token.

```
curl -k https://YourDomainName.cioty.com/helloworld -H "Synx-Cat: 4" -d "token=<your SynxPass token>&objectID=1"
```

```
curl -k https://YourDomainName.cioty.com/helloworld -H "Synx-Cat: 1" -d "token=<your SynxPass token>&objectID=3&txt=Hello World"
```

Lesson in the tutorial: you always need your token and an objectID. You can send and receive what the schema defines.

A longer variant in the tech-corner tutorial allocates ghosts from the Ghosts menu, twice, producing names like nornir.cioty.com/helloworld##1. The double hash marks the object id. Schema there uses an RTW root and a txt element. Idle timeout 60 seconds. The receiver uses Synx-Cat 4 and objectID 2. The sender uses Synx-Cat 1, objectID 1, and txt. The received body looks like:

```xml
<RTW>
<TXT>Hello World</TXT>
</RTW>
```

## A link between two services

Second service named Friend at https://YourDomainName.cioty.com/friend

```xml
<rtw>
<name></name>
</rtw>
```

Timeout 120 seconds. Five ghosts.

Then change HelloWorld so txt is a link:

```xml
<rtw>
<txt>@YourDomainName.cioty.com/friend#name@</txt>
</rtw>
```

The @ signs wrap the linking path. Send a name to Friend with Synx-Cat 1. Listen on HelloWorld with Synx-Cat 4. HelloWorld prints the name that was sent to Friend.

The tech-corner link example uses a schema element whose value is the path:

```xml
<RTW>
<data></data>
<data2>@nornir/helloworld#txt@</data2>
</RTW>
```

MAD, in that tutorial, requires one ghost on HelloUniverse to be morphed by one ghost from HelloWorld before the linked value arrives in data2. Copy the ghost URI of helloworld##1 into HelloUniverse object 2. Then Synx-Cat 4 on HelloUniverse and Synx-Cat 1 on HelloWorld. The output is the Hello World text inside DATA2.

## Command schema

On the Friend service:

```xml
<cmd>
<action></action>
<parameter1></parameter1>
</cmd>
```

The tutorial's example actions are first_name, last_name, and both_names, with parameter1 true or false, to change how the name element prints. The part that set up the link is the only one who can send commands at the target.

Send with Synx-Cat 0. That is a command message. The tutorial says only a service-provider owner with an active link in the opposite direction can do it. Consumers who only own a network resource cannot use the command schema.

```
curl -k https://YourDomainName.cioty.com/friend -H "Synx-Cat: 0" -d "token=<your SynxPass token>&objectID=5&action=first_name&parameter1=true"
```

Listen with Synx-Cat 4.

## Predicates

Inline JavaScript. Two methods on master:

```javascript
master.getValueByElement("element_name");
master.updateValueOnElement("element_name", "string");
```

Example from the short tutorial, after adding uppercase_name beside the link:

```javascript
var string = master.getValueByElement("TXT");
if (string != null) master.updateValueOnElement("UPPERCASE_NAME", string.toUpperCase());
```

The script runs inside a memory container. Loops and miscellaneous code are not allowed. Keep it small. Heavier work belongs in a software agent, a master-worker pattern over websocket.

Predicate transforms data into the local structure before it is sent to primary clients and to secondary services with an active link. Predicate noun runs after the local ghost has the message, and only changes what secondary services with an active link receive. The primary service still gets the schema as defined.

A longer Celsius example uses getValueByElement("CELSIUS") and writes FAREN and KELVIN. The conversion formulas in that note are their example script, including a Kelvin formula that does not match the standard conversion. Do not present that formula as physics.

## Why two messages

If you own the service, you receive one message from ghost zero and one from the objectID in the header. Ghost zero stays with the service provider even after other ghosts are given away. Another user who owns one ghost gets one message.

## Limits named for Cioty

Up to 5 services per domain on the Cioty trial. Pro or enterprise, a private HIVE, has no service limit in this note. Links: up to 5 per element on Cioty, up to 10 on the pro package, unlimited on enterprise.

JSON: yes, by a Synx command, on HTTP or websocket, without this note pasting the command. Do not invent the command name.

Where to store data: the network does not store it. A software agent you run may log data you are allowed to store, meaning data that belongs to you.

Inline script versus agent: use an agent for heavy computation when you do not own the private HIVE. The HIVE owner can add CPU and memory because they have lower-stack access.

Changing a schema does not create a logical dependency. Connected resources with the right signature get the new data. Consumers can leave. The note calls the network survival of the fittest.

Root domain: Cioty is one root. A unique root domain, in this note, means contacting Nornir to map a public IP. Subdomains are the light introduction. Cross-linking services across HIVE networks is how they say the heterogeneous Real Time Web is built.

## Service settings in the domain tool

Name has no spaces, because it is part of the URL. Schema is XML, elements with a start and end, wrapped in RTW. Example:

```xml
<RTW>
<temperature></temperature>
<location></location>
</RTW>
```

A link inside an element:

```xml
<location>@nornir.cioty.com/place#loc@</location>
```

Several links can sit on one element, within the package limits above.

Command schema starts and ends with cmd. Example shape:

```xml
<cmd>
<turn_on></turn_on>
</cmd>
```

The source's example markup was missing a slash on the closing tag. Timeout is seconds since the last message.

Micropage is the auto-generated HTML for a normal browser request. The template cannot be changed. Describe the public data elements there. You may add a product-image link.

Ghosts: add from the ghost pool. Default id is numeric. mapID can replace it, including a blockchain token as the id. Transfer ownership from the ghost. Read access: add a receiver by email. Kill connection is only on a primary service and forces re-authentication. You can remove only your own ghosts.

## Cost claims in the summary

Unverified. This summary says practical tests showed development and maintenance cost reduced by 50 times versus message queues and centralized hubs, and network traffic reduced by more than 50 percent because data is shared on changes and only to an active recipient. Do not state those figures as measurements.

Also claimed here, still their summary: no preinstalled program on a shipped device; the device is integrated into a third-party service ad hoc; ownership of devices can be transferred when someone moves house; links replace APIs so integration is minutes instead of days; a service can aim at a future device that does not exist yet, the LED-light example, without upgrading the app.
