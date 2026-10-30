# `AVCaptureProprietaryDefaultsSingleton`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 21 instance methods, 17 class methods

## Instance variables

```
* _proprietaryDefaultsSourceQueueLabel;
Q _proprietaryDefaultsSourceQueueLabelLength;
@"NSObject<OS_dispatch_queue>" _proprietaryDefaultsSourceQueue;
@"NSObject<OS_dispatch_queue>" _proprietaryDefaultChangeNotificationCallbackQueue;
^{OpaqueFigCaptureSource=} _proprietaryDefaultsSource;
@"AVWeakReference" _weakReference;
@"NSMutableDictionary" _defaultChangedHandlersForObserversForKeys;
@"NSMutableArray" _keyObservationsThatFailedToRegisterWithServer;
```

## Class methods

```
+[AVCaptureProprietaryDefaultsSingleton updateCameraHistory:withCameraInfo:maxLength:updateCameraHistoryDownplayOverrideList:cameraCanBeInOverrideList:];
+[AVCaptureProprietaryDefaultsSingleton initialize];
+[AVCaptureProprietaryDefaultsSingleton cameraHistoryDownplayOverrideList];
+[AVCaptureProprietaryDefaultsSingleton proprietaryDefaultsSingleton];
+[AVCaptureProprietaryDefaultsSingleton addObserver:forKey:callHandlerForInitialValue:defaultChangedHandler:];
+[AVCaptureProprietaryDefaultsSingleton objectForKey:];
+[AVCaptureProprietaryDefaultsSingleton migrateDefaultsFromAppBundleID:newAppBundleID:];
+[AVCaptureProprietaryDefaultsSingleton objectsForWildcardKey:];
+[AVCaptureProprietaryDefaultsSingleton proprietaryDefaultsDomainForAuditToken:];
+[AVCaptureProprietaryDefaultsSingleton imageForKey:fillWidth:fillHeight:];
+[AVCaptureProprietaryDefaultsSingleton removeObserver:forKey:];
+[AVCaptureProprietaryDefaultsSingleton updateCameraOverrideHistory:withCameraInfo:setOverride:];
+[AVCaptureProprietaryDefaultsSingleton setObject:forKey:];
+[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:];
+[AVCaptureProprietaryDefaultsSingleton retryPriorFailedKeyObservationRegistrations];
+[AVCaptureProprietaryDefaultsSingleton proprietaryDefaultsDomainForClient];
+[AVCaptureProprietaryDefaultsSingleton updateProprietaryDefaultsSource];
```

## Instance methods

```
-[AVCaptureProprietaryDefaultsSingleton _handleNotification:payload:];
-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:];
-[AVCaptureProprietaryDefaultsSingleton updateCameraHistory:withCameraInfo:maxLength:updateCameraHistoryDownplayOverrideList:cameraCanBeInOverrideList:];
-[AVCaptureProprietaryDefaultsSingleton init];
-[AVCaptureProprietaryDefaultsSingleton dealloc];
-[AVCaptureProprietaryDefaultsSingleton cameraHistoryDownplayOverrideList];
-[AVCaptureProprietaryDefaultsSingleton addObserver:forKey:callHandlerForInitialValue:defaultChangedHandler:];
-[AVCaptureProprietaryDefaultsSingleton unobserveChangesForKey:];
-[AVCaptureProprietaryDefaultsSingleton objectForKey:];
-[AVCaptureProprietaryDefaultsSingleton migrateDefaultsFromAppBundleID:newAppBundleID:];
-[AVCaptureProprietaryDefaultsSingleton objectsForWildcardKey:];
-[AVCaptureProprietaryDefaultsSingleton _registerWithServerToObserveKey:];
-[AVCaptureProprietaryDefaultsSingleton proprietaryDefaultsDomainForAuditToken:];
-[AVCaptureProprietaryDefaultsSingleton imageForKey:fillWidth:fillHeight:];
-[AVCaptureProprietaryDefaultsSingleton removeObserver:forKey:];
-[AVCaptureProprietaryDefaultsSingleton updateCameraOverrideHistory:withCameraInfo:setOverride:];
-[AVCaptureProprietaryDefaultsSingleton setObject:forKey:];
-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:];
-[AVCaptureProprietaryDefaultsSingleton retryPriorFailedKeyObservationRegistrations];
-[AVCaptureProprietaryDefaultsSingleton _runBlockOnProprietaryDefaultsSourceQueueSync:];
-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:];
```
