# `SBAVSystemControllerCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 10 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _callOutQueue;
@"NSNotificationCenter" _notificationCenter;
@? _dataProviderInitializer;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSHashTable" _queue_observers;
@"AVOutputContext" _queue_outputContext;
@"<SBAVSystemControllerDataProviding>" _queue_dataProvider;
@"NSMutableDictionary" _notificationToHandlerMap;
@"NSMutableDictionary" _notificationToBackgroundQueryCancellationSignalMap;
B _queue_initialized;
@"BSAtomicSignal" _queue_serverDeathSignal;
B _queue_fullyMuted;
B _queue_ringerMuted;
B _queue_audioSessionPlaying;
B _queue_airplayDisplayActive;
@"NSString" _queue_activeCategoryName;
@"NSString" _queue_activeAudioRoute;
@"NSDictionary" _queue_activeAudioRouteInfo;
@"NSArray" _queue_pickableRoutes;
@"NSArray" _queue_activeOutputDevices;
B _outputContextSupportsMultipleOutputDevices;
@"NSObject<OS_dispatch_queue>" _backgroundQueryQueue;
@"NSObject<OS_dispatch_workloop>" _avscOperationsWorkloop;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_workloop>",R,N,V_avscOperationsWorkloop) avscOperationsWorkloop;
@property (TB,R,D,N,GisFullyMuted) fullyMuted;
@property (TB,R,D,N,GisRingerMuted) ringerMuted;
@property (TB,R,D,N,GisAudioSessionPlaying) audioSessionPlaying;
@property (TB,R,D,N,GisAirplayDisplayActive) airplayDisplayActive;
@property (T@"NSString",R,C,D,N) activeCategoryName;
@property (T@"NSString",R,C,D,N) activeAudioRoute;
@property (T@"NSDictionary",R,C,D,N) activeAudioRouteInfo;
@property (T@"NSArray",R,C,D,N) pickableRoutes;
@property (T@"NSArray",R,C,D,N) activeOutputDevices;
```

## Class methods

```
+[SBAVSystemControllerCache sharedInstance];
```

## Instance methods

```
-[SBAVSystemControllerCache _queue_updateActiveAudioRouteFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache _queue_updateRingerMutedFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache init];
-[SBAVSystemControllerCache _queue_updateActiveCategoryNameFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache _queue_rebuildCache];
-[SBAVSystemControllerCache dealloc];
-[SBAVSystemControllerCache activeAudioRouteInfo];
-[SBAVSystemControllerCache _queue_signalBackgroundQueryCancellationForNotification:];
-[SBAVSystemControllerCache activeCategoryName];
-[SBAVSystemControllerCache _queue_updateAirplayDisplayActiveFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache avscOperationsWorkloop];
-[SBAVSystemControllerCache pickableRoutes];
-[SBAVSystemControllerCache initWithCallOutQueue:notificationCenter:dataProviderInitializer:];
-[SBAVSystemControllerCache activeOutputDevices];
-[SBAVSystemControllerCache _backgroundQueryQueue_rebuildDataProvider];
-[SBAVSystemControllerCache isAudioSessionPlaying];
-[SBAVSystemControllerCache addObserver:];
-[SBAVSystemControllerCache _receiveUpdatedValueFromNotification:];
-[SBAVSystemControllerCache isFullyMuted];
-[SBAVSystemControllerCache _queue_backgroundQueryCancellationSignalForNotificationCreatingIfNecessary:];
-[SBAVSystemControllerCache _queue_notifyObserversWithBlock:];
-[SBAVSystemControllerCache _queue_updateActiveOutputDevicesFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache isRingerMuted];
-[SBAVSystemControllerCache _queue_finishRebuildingCacheWithDataProvider:serverDeathSignal:];
-[SBAVSystemControllerCache _queue_updatePickableRoutesFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache _queue_updateFullyMutedFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache _queryActiveOutputDevicesFromContext:];
-[SBAVSystemControllerCache fetchPickableRoutesWithCompletion:];
-[SBAVSystemControllerCache isAirplayDisplayActive];
-[SBAVSystemControllerCache _serverDied:];
-[SBAVSystemControllerCache _queue_updateAudioSessionPlayingFromNotification:allowingBackgroundQueries:backgroundQueriesCancelledBlock:cancelBackgroundQueriesBlock:completion:];
-[SBAVSystemControllerCache activeAudioRoute];
```
