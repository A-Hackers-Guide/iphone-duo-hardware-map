# `NWMonitor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLSessionTaskDelegate`
- 10 instance variables, 15 properties, 30 instance methods, 8 class methods

## Instance variables

```
I _mID;
q _status;
@"NWNetworkDescription" _bestAvailableNetworkDescription;
@"NSArray" _networkDescriptionArray;
@"NWEndpoint" _endpoint;
@"NWParameters" _parameters;
@"NWPathEvaluator" _pathEvaluator;
@"NSUUID" _lastProbeUUID;
@"NSURL" _lastProbeURL;
@"NWInterface" _interface;
```

## Properties

```
@property (Tq,V_status) status;
@property (T@"NWNetworkDescription",&,V_bestAvailableNetworkDescription) bestAvailableNetworkDescription;
@property (T@"NSArray",&,V_networkDescriptionArray) networkDescriptionArray;
@property (T@"NWParameters",&,V_parameters) parameters;
@property (T@"NWEndpoint",&,V_endpoint) endpoint;
@property (T@"NWPathEvaluator",&,V_pathEvaluator) pathEvaluator;
@property (T@"NSUUID",&,V_lastProbeUUID) lastProbeUUID;
@property (T@"NSURL",&,V_lastProbeURL) lastProbeURL;
@property (T@"NWInterface",&,V_interface) interface;
@property (TI,V_mID) mID;
@property (T@"NSString",R,N) privateDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NWMonitor initialize];
+[NWMonitor queue];
+[NWMonitor automaticallyNotifiesObserversForKey:];
+[NWMonitor copySavedMonitorForNetworkDescriptionArray:endpoint:parameters:];
+[NWMonitor mainOperationQueue];
+[NWMonitor monitorWithNetworkDescription:endpoint:parameters:];
+[NWMonitor monitorWithNetworkDescriptionArray:endpoint:parameters:];
+[NWMonitor saveMonitor:];
```

## Instance methods

```
-[NWMonitor parameters];
-[NWMonitor bestAvailableNetworkDescription];
-[NWMonitor mID];
-[NWMonitor setLastProbeURL:];
-[NWMonitor observeValueForKeyPath:ofObject:change:context:];
-[NWMonitor networkDescriptionArray];
-[NWMonitor setEndpoint:];
-[NWMonitor URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:];
-[NWMonitor setParameters:];
-[NWMonitor dealloc];
-[NWMonitor setBestAvailableNetworkDescription:];
-[NWMonitor endpoint];
-[NWMonitor status];
-[NWMonitor setInterface:];
-[NWMonitor pathEvaluator];
-[NWMonitor setNetworkDescriptionArray:];
-[NWMonitor privateDescription];
-[NWMonitor descriptionWithIndent:showFullContent:];
-[NWMonitor interface];
-[NWMonitor setLastProbeUUID:];
-[NWMonitor lastProbeUUID];
-[NWMonitor hash];
-[NWMonitor description];
-[NWMonitor setMID:];
-[NWMonitor lastProbeURL];
-[NWMonitor setStatus:];
-[NWMonitor setPathEvaluator:];
-[NWMonitor evaluateStartingAtIndex:probeUUID:probeWasSuccessful:];
-[NWMonitor isEqual:];
-[NWMonitor matchesNetworkDescriptionArray:endpoint:parameters:];
```
