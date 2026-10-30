# `NWPathEvaluator`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 20 instance methods, 5 class methods

## Instance variables

```
@"NWEndpoint" _endpoint;
@"NSObject<OS_nw_path_evaluator>" _internalEvaluator;
@"NWPath" _internalPath;
```

## Properties

```
@property (T@"NSObject<OS_nw_path_evaluator>",R,V_internalEvaluator) internalEvaluator;
@property (T@"NWPath",&,V_internalPath) internalPath;
@property (T@"NWParameters",R) parameters;
@property (T@"NWPath",R,N) path;
@property (T@"NWEndpoint",R,N,V_endpoint) endpoint;
```

## Class methods

```
+[NWPathEvaluator sharedDefaultEvaluator];
+[NWPathEvaluator savePathEvaluator:];
+[NWPathEvaluator initialize];
+[NWPathEvaluator copySavedPathEvaluatorForEndpoint:parameters:];
+[NWPathEvaluator automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[NWPathEvaluator parameters];
-[NWPathEvaluator setInternalPath:];
-[NWPathEvaluator init];
-[NWPathEvaluator requestNexus];
-[NWPathEvaluator dealloc];
-[NWPathEvaluator matchesEndpoint:parameters:];
-[NWPathEvaluator endpoint];
-[NWPathEvaluator initWithListenParameters:];
-[NWPathEvaluator internalEvaluator];
-[NWPathEvaluator initWithEvaluator:];
-[NWPathEvaluator triggerPathAgentsIncludingVoluntary:withCompletionHandler:];
-[NWPathEvaluator triggerVoluntaryPathAgentsWithCompletionHandler:];
-[NWPathEvaluator internalPath];
-[NWPathEvaluator hash];
-[NWPathEvaluator satisfyPathAgentsWithCompletionHandler:];
-[NWPathEvaluator initWithBrowseDescriptor:parameters:];
-[NWPathEvaluator initWithEndpoint:parameters:];
-[NWPathEvaluator isEqual:];
-[NWPathEvaluator copyPath];
-[NWPathEvaluator path];
```
