# `SDUDisplayRegionBlankingController`

- Image: [`/System/Library/PrivateFrameworks/SystemUIDisplayUtilities.framework/SystemUIDisplayUtilities`](../userland/System__Library__PrivateFrameworks__SystemUIDisplayUtilities.framework__SystemUIDisplayUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _blankingState;
@"NSArray" _blankingBundleIDs;
@"NSMutableOrderedSet" _displayRegionBlankingAssertions;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"NSString" _regionIdentifier;
@"<SDUDisplayRegionBlankingControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSString",R,N,V_regionIdentifier) regionIdentifier;
@property (TQ,R,N) blankingState;
@property (T@"<SDUDisplayRegionBlankingControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SDUDisplayRegionBlankingController dealloc];
-[SDUDisplayRegionBlankingController setDelegate:];
-[SDUDisplayRegionBlankingController delegate];
-[SDUDisplayRegionBlankingController regionIdentifier];
-[SDUDisplayRegionBlankingController _liveBundleIDs];
-[SDUDisplayRegionBlankingController _waitForPendingDeliveries];
-[SDUDisplayRegionBlankingController acquireDisplayRegionBlankingAssertionForReason:restrictingToBundleIDs:];
-[SDUDisplayRegionBlankingController blankingState];
-[SDUDisplayRegionBlankingController initWithRegionIdentifier:delegate:];
```
