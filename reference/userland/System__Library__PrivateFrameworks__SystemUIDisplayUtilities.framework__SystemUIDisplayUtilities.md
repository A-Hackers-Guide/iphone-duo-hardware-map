# `/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`

iOS 27.2 dyld shared cache image. Version `104.100.0.0.0`. **[DSC]**

## Linked libraries (26)

- `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`
- `/System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/PrivateFrameworks/PrototypeTools.framework/PrototypeTools`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftCoreImage.dylib`
- `/usr/lib/swift/libswiftCoreLocation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftMetal.dylib`
- `/usr/lib/swift/libswiftOSLog.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftQuartzCore.dylib`
- `/usr/lib/swift/libswiftSpatial.dylib`
- `/usr/lib/swift/libswiftUniformTypeIdentifiers.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswift_Concurrency.dylib`
- `/usr/lib/swift/libswiftos.dylib`
- `/usr/lib/swift/libswiftsimd.dylib`

## Objective-C: 13 classes, 9 protocols, 138 methods, 32 properties

### Class pages

Every class and protocol, with its methods: [`BSInvalidatable`](../objc/BSInvalidatable_SystemUIDisplayUtilities.protocol.md), [`BSServiceConnectionListenerDelegate`](../objc/BSServiceConnectionListenerDelegate_SystemUIDisplayUtilities.protocol.md), [`NSObject`](../objc/NSObject_SystemUIDisplayUtilities.protocol.md), [`PTSettingsKeyPathObserver`](../objc/PTSettingsKeyPathObserver_SystemUIDisplayUtilities.protocol.md), [`SDUDisplayBlankingDescription`](../objc/SDUDisplayBlankingDescription_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingAssertion`](../objc/SDUDisplayRegionBlankingAssertion_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingClientToServerInterface`](../objc/SDUDisplayRegionBlankingClientToServerInterface_SystemUIDisplayUtilities.protocol.md), [`SDUDisplayRegionBlankingController`](../objc/SDUDisplayRegionBlankingController_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingControllerDelegate`](../objc/SDUDisplayRegionBlankingControllerDelegate_SystemUIDisplayUtilities.protocol.md), [`SDUDisplayRegionBlankingCoordinator`](../objc/SDUDisplayRegionBlankingCoordinator_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingCoordinatorWindow`](../objc/SDUDisplayRegionBlankingCoordinatorWindow_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingObserver`](../objc/SDUDisplayRegionBlankingObserver_SystemUIDisplayUtilities.protocol.md), [`SDUDisplayRegionBlankingPrototypeSettings`](../objc/SDUDisplayRegionBlankingPrototypeSettings_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingPrototypeSettingsDomain`](../objc/SDUDisplayRegionBlankingPrototypeSettingsDomain_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingRenderer`](../objc/SDUDisplayRegionBlankingRenderer_SystemUIDisplayUtilities.protocol.md), [`SDUDisplayRegionBlankingServerToClientInterface`](../objc/SDUDisplayRegionBlankingServerToClientInterface_SystemUIDisplayUtilities.protocol.md), [`SDUDisplayRegionBlankingService`](../objc/SDUDisplayRegionBlankingService_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingServiceServer`](../objc/SDUDisplayRegionBlankingServiceServer_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingServiceSpecification`](../objc/SDUDisplayRegionBlankingServiceSpecification_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingStateObserverInfo`](../objc/SDUDisplayRegionBlankingStateObserverInfo_SystemUIDisplayUtilities.md), [`SDUDisplayRegionBlankingViewController`](../objc/SDUDisplayRegionBlankingViewController_SystemUIDisplayUtilities.md), [`_TtC24SystemUIDisplayUtilities11GainMapView`](../objc/_TtC24SystemUIDisplayUtilities11GainMapView_SystemUIDisplayUtilities.md)

### Classes

`SDUDisplayBlankingDescription`, `SDUDisplayRegionBlankingAssertion`, `SDUDisplayRegionBlankingController`, `SDUDisplayRegionBlankingCoordinator`, `SDUDisplayRegionBlankingCoordinatorWindow`, `SDUDisplayRegionBlankingPrototypeSettings`, `SDUDisplayRegionBlankingPrototypeSettingsDomain`, `SDUDisplayRegionBlankingService`, `SDUDisplayRegionBlankingServiceServer`, `SDUDisplayRegionBlankingServiceSpecification`, `SDUDisplayRegionBlankingStateObserverInfo`, `SDUDisplayRegionBlankingViewController`, `_TtC24SystemUIDisplayUtilities11GainMapView`

### Protocols

`BSInvalidatable`, `BSServiceConnectionListenerDelegate`, `NSObject`, `PTSettingsKeyPathObserver`, `SDUDisplayRegionBlankingClientToServerInterface`, `SDUDisplayRegionBlankingControllerDelegate`, `SDUDisplayRegionBlankingObserver`, `SDUDisplayRegionBlankingRenderer`, `SDUDisplayRegionBlankingServerToClientInterface`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N,V_regionIdentifier) regionIdentifier;
@property (TQ,R,N,V_blankingState) blankingState;
@property (T@"NSArray",R,C,N,V_bundleIDs) bundleIDs;
@property (TQ,R,N,V_previousBlankingState) previousBlankingState;
@property (T@"NSArray",R,C,N,V_previousBundleIDs) previousBundleIDs;
@property (T@"NSArray",R,C,N,V_bundleIDs) bundleIDs;
@property (T@"NSString",R,N,V_regionIdentifier) regionIdentifier;
@property (TQ,R,N) blankingState;
@property (T@"<SDUDisplayRegionBlankingControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"<SDUDisplayRegionBlankingCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (T@"<SDUDisplayRegionBlankingRenderer>",W,N,V_blankingRenderer) blankingRenderer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N,Vregion1Width) region1Width;
@property (Td,N,Vregion1Height) region1Height;
@property (Td,N,Vregion1CornerRadius) region1CornerRadius;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SDUDisplayRegionBlankingStateObserver>",&,N,V_observer) observer;
@property (TQ,N,V_blankingState) blankingState;
```

## Swift types (5)

`SystemUIDisplayUtilities.DisplayRegionBlankingViewController:`, `SystemUIDisplayUtilities.GainMapView:`, `__C.CGPoint`, `__C.CGRect`, `__C.CGSize`

## Strings (80)

```
SDUDisplayRegionBlankingService.m
init is unsupported -- use +sharedInstance instead
SDUDisplayRegionBlankingController.m
com.apple.springboard.SDUDisplayRegionBlankingController
$
region1CornerRadius
region1Width
%@-region-blanking-state-observer
v16@?0@\"<BSCompoundAssertionState>\"8
com.apple.springboard.display-region-blanking-service
Display Region Blanking
init(nibName:bundle:)
init(coder:) has not been implemented
v16@?0@\"BSSimpleAssertion\"8
v32@?0@\"NSString\"8@\"UIWindowScene\"16^B24
com.apple.SpringBoard.SDUDisplayRegionBlankingServiceServer.connectionQueue
Unknown(%lu)
+new is unsupported -- use +sharedInstance instead
Restore Defaults
System UI Display Utilities
com.apple.SystemUIDisplayUtilities
region1Height
Region1
Invalid condition not satisfying: %@
a
v8@?0
r
v16@?0@\"<BSServiceConnectionConfiguring>\"8
SDUDisplayRegionBlankingService must be invalidated before dealloc
SystemUIDisplayUtilities/GainMapView.swift
v16@?0Q8
v16@?0@\"BSServiceConnection<BSServiceConnectionContext>\"8
SystemUIDisplayUtilities/DisplayRegionBlankingViewController.swift
com.apple.springboard.display-region-blanking
Unblanked
SDUDisplayRegionBlankingService.blankDisplayRegion
<%@:%p>
DisplayRegionBlanking
SystemUIDisplayUtilities.DisplayRegionBlankingViewController
Fatal error
regionIdentifier != ((void*)0)
com.apple.frontboard
v16@?0@\"<BSServiceConnectionListenerConfiguring>\"8
Blanked
setInProcessCoordinator: called more than once; this is unsupported
com.apple.SystemUIDisplayUtilities.SDUDisplayRegionBlankingServiceClient.connectionQueue
com.apple.SystemUIDisplayUtilities.SDUDisplayRegionBlankingControllerDelegate.connectionQueue
reason != ((void*)0)
, 
v16@?0@\"BSServiceConnection\"8
SDUDisplayRegionBlankingServiceServer: setting blanking controller for invalid region %{public}@
SDUDisplayRegionBlankingServiceServer: invalidateDisplayRegionBlankingAssertionWithUniqueIdentifier: denied due to client's lack of entitlement (%@)
DisplayRegionBlankingViewController: Showing blanking view for region '%s'
SDUDisplayRegionBlankingServiceServer: assertion invalidation requested by %@ for region '%@' uniqueIdentifier %@
DisplayRegionBlankingViewController: Hiding blanking view for region '%s'
DisplayRegionBlankingViewController: %s blanking view for region '%s'
SDUDisplayRegionBlankingCoordinator: '%@' region transitioning to blanking state: %@
SDUDisplayRegionBlankingServiceServer: Invalidating %lu assertions for disconnected connection %@
SDUDisplayRegionBlankingService: connection invalidated remotely. (Do you have the required entitlement?)
DisplayRegionBlankingViewController: Updating region frame to %s with corner radius %f
SDUDisplayRegionBlankingServiceServer: nil arguments to invalidateDisplayRegionBlankingAssertionWithUniqueIdentifier: uniqueIdentifier %@ regionIdentifier %@
SDUDisplayRegionBlankingServiceServer: nil arguments to setBlankingStateObservationEnabled: enabledNumber %@ regionIdentifier %@
SDUDisplayRegionBlankingController: assertion destroyed for region '%@' reason '%@' bundleIDs (%@) (remaining assertions: %lu)
SDUDisplayRegionBlankingController: '%@' region cannot be blanked by bundleIDs: (%@)
SDUDisplayRegionBlankingServiceServer: acquireDisplayRegionBlankingAssertionWithUniqueIdentifier: denied due to client's lack of entitlement (%@)
SDUDisplayRegionBlankingServiceServer invalidating connection because client process is missing required entitlement %@ .
SDUDisplayRegionBlankingServiceServer: nil arguments to blankingStateForDisplayRegion: regionIdentifier %@
failure in %{public}@ of <%{public}@:%p> (%{public}@:%i) : %{public}@
SDUDisplayRegionBlankingServiceServer interrupted/invalidated connection %@
SDUDisplayRegionBlankingServiceServer: blankingStateForDisplayRegion: denied due to client's lack of entitlement (%@)
SDUDisplayRegionBlankingServiceServer activated connection %@
SDUDisplayRegionBlankingServiceServer: assertion requested by %@ for region '%@' uniqueIdentifier %@ reason '%@' bundleIDs (%@)
SDUDisplayRegionBlankingController: assertion granted for region '%@' reason '%@' bundleIDs (%@) (total assertions: %lu)
SDUDisplayRegionBlankingServiceServer: nil arguments to acquireDisplayRegionBlankingAssertionWithUniqueIdentifier: uniqueIdentifier %@ regionIdentifier %@ reason %@
SDUDisplayRegionBlankingServiceServer: setBlankingStateObservationEnabled: denied due to client's lack of entitlement (%@)
SDUDisplayRegionBlankingServiceServer: Invalidating assertion %@ for region '%@' due to connection disconnect
SDUDisplayRegionBlankingService: initialized in in-process mode
SDUDisplayRegionBlankingService: connection interrupted. Reactivating connection.
SDUDisplayRegionBlankingCoordinator: '%@' region bundle IDs changed while blanked: (%@)
SDUDisplayRegionBlankingCoordinator: Region 1 settings changed - %@: %@
```
