# Real Time Web — Web Content and Q&A

Source: web-content document dated 2026 in the master export. Site structure, conceptual copy, FAQ, and editorial guidance for RealTimeWeb.org, Morph.Space, and Synx tools. Many Morph Space and Synx tool questions in this file were still pending. The live 2026 sites may have answered some of them later. Prefer the public page when they conflict. Sections marked draft here are not final.

## Status and homes

Answered means the source had a written answer. Pending means listed with no answer, or only a placeholder. Draft means it needs team review before publishing.

RealTimeWeb.org: what RTW is and how it works. Neutral, specification-oriented. Main action: understand or implement.

Morph.Space: what users can do and how they join. Accessible and commercial. Main action: create an account or domain.

Synx documentation: how each tool is configured. Technical. Main action: administer the network.

Help Center: troubleshooting. Direct. Main action: resolve a problem.

Canonical homes: conceptual questions on RealTimeWeb.org. Account, marketplace, and onboarding on Morph.Space. Configuration and operations in Synx documentation.

On Morph Space, "What is the Real Time Web?" should get two sentences, then a pointer to RealTimeWeb.org.

Every FAQ answer should ideally have three levels: a direct first sentence, two or three sentences of explanation, and a link to a guide or specification.

## Crucial distinction

Real Time Web defines the network. Morph Space provides a way to join and participate in it. Synx tools provide the controls needed to configure, secure, and operate it.

The source says this clarification should appear prominently, and that placement and final wording need team approval:

Real Time Web is a network concept and architecture. Morph Space is a commercial platform and reference implementation that allows people and organizations to join and use the network.

## Draft architecture notes

These subsections were marked draft. Treat them as working notes.

Network topology: MAD constructs data channels from sources that have been morphed along the linking path. Each service operates on local data and can only persist and access data in local context. How data is morphed outside that service is unknown there. There is no centralized API or database when building RTW services. Data is consumed at the endpoint only when the ghost at both ends is owned by the same user.

Identity: when ghosts are first allocated they are owned by the service owner. After a user registers, the service owner can transfer the ghost id. When the user approves, the user controls the data layer of that ghost. The service itself is also a ghost in the application layer, and that ownership can be transferred separately. Four layers of ownership can change independently. Authentication is optional in the design. This note says the only implementation then in use was SynxPass, part of Synx Tools, used by Morph Space.

Domains: MAD is a bijective network. Even an endpoint that cannot keep a connection alive can receive program execution and data from its ghost. This note calls that kernelization, and says it lets empathy devices connect and get a program once activated, and lets AI agents activate the endpoint. The ghostID can be mapped to the MAC address.

Data channels: a linking path collects sources into a channel. Example: a service collects temperature from several manufacturers. Only a valid morphed ghost receives data.

Discovery: the stack is distributed to the endpoint on activation. Before that, the endpoint need not contain a protocol, library, or predefined program. This note says the current implementation is Synx.tools and Morph.Space, based on TCP/IP for the stateful connection and HTTPS and websocket for the protocol. An endpoint can connect with native TCP and send or receive using HTTPS or websocket.

Authentication draft: Synx Pass is token based. The endpoint needs to refresh the token every three minutes to send data. This interval is a draft note, not a 2026 public specification.

Ownership: whoever owns the ghostId owns the data at that endpoint. The application-layer ghost belongs to the service owner, including morphed data and command data. Ghost id zero is the service. The service owner can transfer ghost id zero.

Protocols draft: Synx BIOS supports XML and JSON. Default is XML. A synx command can switch to JSON at runtime without dropping the connection, by a client that has domain ownership. RTW is protocol independent. The service owner decides the protocol. The micropage describes the service and data model. If a micropage lacks structured information, this note says the provider is not serious and should not be linked to.

Interoperability: linking a source and transforming it to the local model is the normalizer. Offering changes after the local model updates is the materializer. Kernelizer sends a self-contained message before the data stream so the client can build its interface without a preinstalled program. The endpoint can be an empty container. Program and data are deployed later.

Security draft: MAD does not natively persist data into databases or filesystems. The network is tokenized. This note says any token system such as blockchain, Keycloak, or another token issuer can be used. Reference implementation named here: Morph.space using SynxPass from Synx (synx.tools).

## Answered ownership questions

Who owns data: the user who controls the endpoint and registered it against the endpoint ghost. The ghost can be transferred. Morphing the ghost against a secondary service gives the service provider read access. The owner can withdraw that read access. When a Morphic service is created, the service owner is the primary owner of allocated ghosts. After the user confirms the transfer, the data layer belongs to the user. The application layer still belongs to the service owner, who always has access to a local copy.

Where data is stored: not natively in the network. It is morphed into local data models along the linking path. A service owner who has been given the data may persist it in that local context. For data to be consumed at the endpoint, the sender and receiver ghosts need an owner with ownership or read access. A service provider with read access to many users may decide to share further. This note says that provider has to be trusted.

How access is authorized: Morph Space uses Synx Pass.

How access is revoked: by a token revocation endpoint. Time-based revocation policies have been set, and terminating user sessions can be activated through Synx runtime BIOS. This note does not give the endpoint URL or the payload. Do not invent them.

How identities are protected: a ghost is a proxy for the network resource, in multiple layers, bijectively connected. It provides identity, behavior, and context when a connection is present.

GDPR: the user controls who has access, and data is not persisted in the network space unless the user has agreed. The user can morph a ghost into a secondary service and share, and can stop.

## Pending questions in this plan

Do not answer these as settled from this file. Related draft notes exist above and still needed approval.

Architecture, unanswered here: how the topology works; what bijective network architecture means; how services, devices, and AI agents are identified; what an RTW domain is; what a real-time data channel is; how data is exchanged; whether centralized servers are required; how traffic is reduced.

Standards, unanswered here: whether RTW is an open specification; whether other companies can build compatible implementations; which specifications exist; how they are versioned; how to contribute; whether there is a reference implementation; where technical documentation is.

Morph Space FAQ in this file is unanswered unless noted: what Morph Space is; how it relates to RTW; whether it is the same as RTW; who can use it; what you can build; how to join; whether you need a domain name; whether you can register or connect a domain; how long setup takes; whether you need technical experience; multiple administrators; connecting an existing app, IoT, or AI agents; languages; API or SDK; sandbox; examples; marketplace; charging for data; who sets the price; subscriptions; Morph Space fee; free access; who owns published data; free plan; cost; upgrade or cancel; enterprise; support.

One pending line, "How quickly can I get my morph_space up and running?", pointed at a Hostinger VPS article, not an RTW answer: https://www.hostinger.com/support/8852211-how-soon-will-your-vps-be-set-up-and-ready-for-use-at-hostinger/ Do not treat that as the RTW setup time.

Synx tool FAQs in this plan were also unanswered, including Synx DNS, Synx BIOS, Synx Pass, and runtime administration. Editorial rule: because BIOS already means PC firmware, the first answer should say the RTW meaning and distinguish it.

Suggested order in the source: glossary, then the boundary between RTW, Morph Space, and each tool, then the RealTimeWeb.org overview, then Morph Space onboarding, then 8 to 10 homepage FAQs, then per-tool docs, then troubleshooting from real support requests.
