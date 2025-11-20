**Challenge Statement**

Managing customer support for an online car parts retailer is becoming increasingly complex and time-consuming. <br/>
The customer service team receives 100+ daily inquiries about car parts compatibility and car service appointments. <br/>
The current manual process requires to search in the database and sometimes coordination with multiple departments, leading to unpredictable response time and inconsistent customer experiences.

**Solution**

Build an automated Multi-Agent Customer Support System that handles customer inquiries end-to-end, reducing human intervention, while providing accurate, personalized responses across the board.

**Value Proposition**

This multi-agent system will reduce customer support response time from 10-30 min to under 5 minutes, decreasing operational costs by at least 50%, and improve customer satisfaction by at least 20%, through fast and accurate responses.

**Architecture**
- Two sequential specialized agents powered by an LLM.
- A2A Protocol for agent-to-agent routing.
- Two custom tools.
- Sessions & state management (InMemorySessionService).
- Observability.
- Test cases to evaluate the agents performance.
