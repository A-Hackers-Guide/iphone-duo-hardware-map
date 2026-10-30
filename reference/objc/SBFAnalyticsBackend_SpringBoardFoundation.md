# `SBFAnalyticsBackend`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFAnalyticsBackendEventHandling`
- 5 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _asyncEventHandlers;
@"NSMutableArray" _syncEventHandlers;
@"NSMutableDictionary" _stateQueryHandlers;
@"NSObject<OS_dispatch_queue>" _queryHandlerQueue;
@"NSObject<OS_dispatch_queue>" _asyncHandlerQueue;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFAnalyticsBackend sharedInstance];
```

## Instance methods

```
-[SBFAnalyticsBackend init];
-[SBFAnalyticsBackend registerEventHandler:];
-[SBFAnalyticsBackend handleEvent:withContext:];
-[SBFAnalyticsBackend registerForQueryName:handler:];
-[SBFAnalyticsBackend registerSynchronousEventHandler:];
-[SBFAnalyticsBackend stateForQueryName:completion:];
```
