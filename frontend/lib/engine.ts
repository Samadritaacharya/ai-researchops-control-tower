export type Metric={label:string;value:string;detail:string;tone:'good'|'warn'|'risk'}
export type RunResult={scenarioId:string;status:'HEALTHY'|'WATCH'|'INTERVENE';score:number;headline:string;metrics:Metric[];signals:string[];recommendations:string[];trace:string[];contextSignals:string[]}
type Scenario={id:string;name:string;summary:string;score:number;pressure:number;headline:string;metrics:Array<{label:string;base:number;slope:number;unit:string;detail:string;inverse?:boolean}>;signals:string[];recommendations:string[]}

export const project={
  slug:'ai-researchops-control-tower',
  name:'AI ResearchOps',
  repoUrl:'https://github.com/Samadritaacharya/ai-researchops-control-tower',
  eyebrow:'AI Delivery Governance · Research Operations',
  title:'Turn uncertain AI work into visible decisions.',
  description:'Explore how intake, uncertainty, RAID, RACI, experiment evidence, governance controls, steering, and handover readiness can be managed as one operating system for AI initiatives.',
  simulatorTitle:'Stress-test an AI initiative.',
  simulatorDescription:'Choose a synthetic delivery state, adjust uncertainty pressure, add context, and run the deterministic governance engine.',
  contextPlaceholder:'Optional: describe privacy concerns, missing owners, weak baselines, security risk, acceptance criteria, or handover dependencies…',
  accent:'#8b5cf6',secondary:'#f472b6',
  nodes:['Intake','Uncertainty','RAID','RACI','Experiments','Steering','Handover'],
  proof:['12 governance modules','Zero required API keys','RAID + RACI','CI-verified Python'],
  scenarios:[
    {id:'prototype-uncertainty',name:'Prototype uncertainty',summary:'A promising prototype has weak ownership, changing scope, and incomplete experiment evidence.',score:66,pressure:24,headline:'The initiative needs structure before it needs more acceleration.',metrics:[
      {label:'Uncertainty',base:74,slope:16,unit:'%',detail:'Composite scope, data, model, and acceptance uncertainty',inverse:true},
      {label:'Risk ownership',base:58,slope:-16,unit:'%',detail:'Risks with explicit accountable owners'},
      {label:'Experiment evidence',base:46,slope:-14,unit:'%',detail:'Baselines, targets, and observed results captured'},
      {label:'Handover readiness',base:34,slope:-12,unit:'%',detail:'Operational ownership and acceptance readiness'},
    ],signals:['Scope and acceptance criteria are still moving.','Experiment learning exists but is not yet strong enough for a handover decision.','Risk ownership is the fastest lever for reducing delivery ambiguity.'],recommendations:['Freeze a testable next milestone and acceptance criteria.','Assign owners to the highest-impact RAID items.','Require a baseline and target before the next experiment review.']},
    {id:'governance-review',name:'Governance review',summary:'The initiative is approaching a release decision with privacy, explainability, and access-control questions.',score:79,pressure:18,headline:'The delivery path is viable if evidence remains attached to the control decisions.',metrics:[
      {label:'Governance coverage',base:84,slope:-10,unit:'%',detail:'Synthetic privacy, quality, explainability, security, and access controls'},
      {label:'Risk ownership',base:88,slope:-8,unit:'%',detail:'Material risks with accountable owners'},
      {label:'Experiment evidence',base:72,slope:-10,unit:'%',detail:'Decision-grade evidence across tracked experiments'},
      {label:'Handover readiness',base:63,slope:-12,unit:'%',detail:'Readiness for operating ownership and support'},
    ],signals:['Governance evidence is stronger than product handover readiness.','Residual risk is concentrated in data handling and operational ownership.','The steering decision can be evidence-based rather than status-based.'],recommendations:['Close the data-handling decision before release approval.','Convert experiment outcomes into explicit go/no-go criteria.','Name the production owner and support model before handover.']},
    {id:'handover-ready',name:'Handover ready',summary:'Evidence, ownership, governance, and acceptance criteria are mature enough for an operational handover decision.',score:91,pressure:12,headline:'The initiative is ready to move from research governance into product ownership.',metrics:[
      {label:'Acceptance criteria',base:94,slope:-6,unit:'%',detail:'Defined and evidenced acceptance conditions'},
      {label:'Risk closure',base:89,slope:-7,unit:'%',detail:'Material risks closed or accepted with owners'},
      {label:'Experiment evidence',base:92,slope:-7,unit:'%',detail:'Experiment trail supporting the release decision'},
      {label:'Handover readiness',base:95,slope:-8,unit:'%',detail:'Ownership, support, documentation, and rollout readiness'},
    ],signals:['Decision evidence is traceable to experiments and acceptance criteria.','Residual risks have owners and explicit treatment.','The operating model is defined before transfer.'],recommendations:['Run the final owner/readiness review.','Capture accepted residual risks in the handover record.','Set a post-launch evidence checkpoint for adoption and model quality.']},
  ] as Scenario[]
}

const clamp=(v:number,min=0,max=100)=>Math.min(max,Math.max(min,v))
const round=(v:number)=>Math.round(v*10)/10
function tone(value:number,inverse=false):Metric['tone']{const n=inverse?100-value:value;return n>=80?'good':n>=62?'warn':'risk'}

export function runSimulation(scenarioId:string,intensity=50,context=''):RunResult{
  const s=project.scenarios.find(x=>x.id===scenarioId)??project.scenarios[0]
  const p=clamp(intensity);const d=(p-50)/50;const contextSignals:string[]=[];let penalty=0
  if(/privacy|bias|security|personal data|residency/i.test(context)){penalty+=6;contextSignals.push('Context introduces an explicit AI-governance risk signal.')}
  if(/no owner|missing owner|unclear owner|dependency|blocked/i.test(context)){penalty+=5;contextSignals.push('Context suggests unresolved ownership or dependency risk.')}
  if(/baseline|acceptance criteria|owner assigned|evidence|signed off/i.test(context)){penalty-=3;contextSignals.push('Context includes decision evidence or explicit ownership.')}
  const score=Math.round(clamp(s.score-d*s.pressure-penalty,20,99));const status:RunResult['status']=score>=80?'HEALTHY':score>=65?'WATCH':'INTERVENE'
  const metrics=s.metrics.map(m=>{const value=round(Math.max(0,m.base+d*m.slope));return{label:m.label,value:`${value}${m.unit}`,detail:m.detail,tone:tone(value,Boolean(m.inverse))} satisfies Metric})
  return{scenarioId:s.id,status,score,headline:s.headline,metrics,signals:s.signals,recommendations:s.recommendations,trace:['Intake signal','Score uncertainty','Resolve RAID ownership','Check experiment evidence','Apply governance controls','Prepare steering view','Assess handover'],contextSignals}
}
