# `PLFSEventAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 2 instance variables, 2 properties, 12 instance methods, 7 class methods

## Instance variables

```
@"PLXPCResponderOperatorComposition" _fileListResponder;
^{__FSEventStream=} _stream;
```

## Properties

```
@property (T@"PLXPCResponderOperatorComposition",&,V_fileListResponder) fileListResponder;
@property (T^{__FSEventStream=},V_stream) stream;
```

## Class methods

```
+[PLFSEventAgent entryEventIntervalDefinitions];
+[PLFSEventAgent entryEventPointDefinitions];
+[PLFSEventAgent entryEventForwardDefinitions];
+[PLFSEventAgent entryEventBackwardDefinitions];
+[PLFSEventAgent entryEventNoneDefinitions];
+[PLFSEventAgent load];
+[PLFSEventAgent entryAggregateDefinitions];
```

## Instance methods

```
-[PLFSEventAgent startMonitoring];
-[PLFSEventAgent stream];
-[PLFSEventAgent init];
-[PLFSEventAgent dealloc];
-[PLFSEventAgent initOperatorDependancies];
-[PLFSEventAgent setStream:];
-[PLFSEventAgent stopMonitoring];
-[PLFSEventAgent addLogFileNameEntry:withType:withName:];
-[PLFSEventAgent fileListResponder];
-[PLFSEventAgent logLogFileName:withName:];
-[PLFSEventAgent registerforFSEventNotification];
-[PLFSEventAgent setFileListResponder:];
```
