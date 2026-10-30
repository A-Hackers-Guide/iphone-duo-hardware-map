# `NWCandidatePathMonitor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 23 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
@"NSObject<OS_nw_path_evaluator>" _primaryEvaluator;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSArray" _remoteEndpoints;
@"NSMutableDictionary" _candidatePathEvaluators;
@? _updateHandler;
```

## Properties

```
@property (T@"NSObject<OS_nw_path_evaluator>",&,N,V_primaryEvaluator) primaryEvaluator;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSArray",&,N,V_remoteEndpoints) remoteEndpoints;
@property (T@"NSMutableDictionary",&,N,V_candidatePathEvaluators) candidatePathEvaluators;
@property (T@?,C,N,V_updateHandler) updateHandler;
@property (T@"NWParameters",R,N) parameters;
@property (T@"NSArray",R,N) interfaces;
@property (T@"NSArray",R,N) candidatePaths;
```

## Instance methods

```
-[NWCandidatePathMonitor updateHandler];
-[NWCandidatePathMonitor setUpdateHandler:];
-[NWCandidatePathMonitor parameters];
-[NWCandidatePathMonitor setPrimaryEvaluator:];
-[NWCandidatePathMonitor initWithParameters:];
-[NWCandidatePathMonitor init];
-[NWCandidatePathMonitor dealloc];
-[NWCandidatePathMonitor queue];
-[NWCandidatePathMonitor interfaces];
-[NWCandidatePathMonitor primaryEvaluator];
-[NWCandidatePathMonitor setQueue:];
-[NWCandidatePathMonitor remoteEndpoints];
-[NWCandidatePathMonitor cParameters];
-[NWCandidatePathMonitor cancelCandidatePathEvaluators];
-[NWCandidatePathMonitor cancelWithHandler:];
-[NWCandidatePathMonitor candidatePathEvaluators];
-[NWCandidatePathMonitor candidatePaths];
-[NWCandidatePathMonitor interfacesLocked];
-[NWCandidatePathMonitor resetCandidatePathEvaluators];
-[NWCandidatePathMonitor setCandidatePathEvaluators:];
-[NWCandidatePathMonitor setRemoteEndpoints:];
-[NWCandidatePathMonitor startWithQueue:updateHandler:];
-[NWCandidatePathMonitor updateRemoteEndpoints:];
```
