# Stateless & Stateful agents
##### *Managing context, cost, and memory*
- managing state is little bit harder now

we want to have a conversation
- very often we want to iterate
- we want to be able to manage a conversation
when we have a conversation we make a lot of assumption on what the other person know 
the things u say to them depends of what you think they know
we need to communicate to people, and we try to optimize the conversation

LLM doesn't know this things, every call 

*we need to manage a conversation*
*we need to manage long-term memory*

Long term memory

New Abstraction:
- "state" and memory management 

we know from the past: Server-Managed State

LLMs are stateless functions.
State could be our responsibility
the model doesn't remember anything - you must send the relevant context with every request. this design choice has profound implication for cost

### 01 Stateless Agent
- single shot task
- independent queries
- serverless functions, webhooks

### 02 Stateful agent
- managing this is simple store the conversation
- this work but its complex, this thing continue to grow and makes difficult for the llm to concentrate on what u need


