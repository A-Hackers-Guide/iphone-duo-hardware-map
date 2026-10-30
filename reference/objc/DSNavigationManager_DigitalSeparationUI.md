# `DSNavigationManager`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _panesRequiringNetwork;
@"NSArray" _detailControllerPanes;
@"NSDictionary" _safetyResetChapters;
@"NSDictionary" _sharingActivityChapters;
@"NSArray" _safetyResetNavigationOrder;
@"NSArray" _sharingActivityNavigationOrder;
@"NSDictionary" _safetyResetChaptersDTO;
@"NSDictionary" _sharingActivityChaptersDTO;
@"NSArray" _safetyResetNavigationOrderDTO;
@"NSArray" _sharingActivityNavigationOrderDTO;
@"NSDictionary" _safetyCheckChaptersWifiSync;
@"NSArray" _safetyCheckNavigationOrderWifiSync;
@"NSDictionary" _reviewDeviceAccessChapters;
@"NSArray" _reviewDeviceAccessNavigationOrder;
@"NSDictionary" _reviewBlockingChapters;
@"NSArray" _reviewBlockingNavigationOrder;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_safetyResetChapters) safetyResetChapters;
@property (T@"NSDictionary",&,N,V_sharingActivityChapters) sharingActivityChapters;
@property (T@"NSArray",&,N,V_safetyResetNavigationOrder) safetyResetNavigationOrder;
@property (T@"NSArray",&,N,V_sharingActivityNavigationOrder) sharingActivityNavigationOrder;
@property (T@"NSDictionary",&,N,V_safetyResetChaptersDTO) safetyResetChaptersDTO;
@property (T@"NSDictionary",&,N,V_sharingActivityChaptersDTO) sharingActivityChaptersDTO;
@property (T@"NSArray",&,N,V_safetyResetNavigationOrderDTO) safetyResetNavigationOrderDTO;
@property (T@"NSArray",&,N,V_sharingActivityNavigationOrderDTO) sharingActivityNavigationOrderDTO;
@property (T@"NSDictionary",&,N,V_safetyCheckChaptersWifiSync) safetyCheckChaptersWifiSync;
@property (T@"NSArray",&,N,V_safetyCheckNavigationOrderWifiSync) safetyCheckNavigationOrderWifiSync;
@property (T@"NSDictionary",&,N,V_reviewDeviceAccessChapters) reviewDeviceAccessChapters;
@property (T@"NSArray",&,N,V_reviewDeviceAccessNavigationOrder) reviewDeviceAccessNavigationOrder;
@property (T@"NSDictionary",&,N,V_reviewBlockingChapters) reviewBlockingChapters;
@property (T@"NSArray",&,N,V_reviewBlockingNavigationOrder) reviewBlockingNavigationOrder;
@property (T@"NSArray",&,N,V_panesRequiringNetwork) panesRequiringNetwork;
@property (T@"NSArray",&,N,V_detailControllerPanes) detailControllerPanes;
```

## Instance methods

```
-[DSNavigationManager init];
-[DSNavigationManager isDTOActive];
-[DSNavigationManager setSafetyCheckChaptersWifiSync:];
-[DSNavigationManager deepLinkToPane:inFlow:];
-[DSNavigationManager detailControllerPanes];
-[DSNavigationManager navigationChaptersForFlowType:];
-[DSNavigationManager navigationForURL:];
-[DSNavigationManager navigationOrderForFlowType:];
-[DSNavigationManager panesRequiringNetwork];
-[DSNavigationManager restoredDTONavigationOrder:withPath:];
-[DSNavigationManager restoredDeviceAccessNavigationOrder:];
-[DSNavigationManager reviewBlockingChapters];
-[DSNavigationManager reviewBlockingNavigationOrder];
-[DSNavigationManager reviewDeviceAccessChapters];
-[DSNavigationManager reviewDeviceAccessNavigationOrder];
-[DSNavigationManager safetyCheckChaptersWifiSync];
-[DSNavigationManager safetyCheckNavigationOrderWifiSync];
-[DSNavigationManager safetyResetChapters];
-[DSNavigationManager safetyResetChaptersDTO];
-[DSNavigationManager safetyResetNavigationOrder];
-[DSNavigationManager safetyResetNavigationOrderDTO];
-[DSNavigationManager setDetailControllerPanes:];
-[DSNavigationManager setPanesRequiringNetwork:];
-[DSNavigationManager setReviewBlockingChapters:];
-[DSNavigationManager setReviewBlockingNavigationOrder:];
-[DSNavigationManager setReviewDeviceAccessChapters:];
-[DSNavigationManager setReviewDeviceAccessNavigationOrder:];
-[DSNavigationManager setSafetyCheckNavigationOrderWifiSync:];
-[DSNavigationManager setSafetyResetChapters:];
-[DSNavigationManager setSafetyResetChaptersDTO:];
-[DSNavigationManager setSafetyResetNavigationOrder:];
-[DSNavigationManager setSafetyResetNavigationOrderDTO:];
-[DSNavigationManager setSharingActivityChapters:];
-[DSNavigationManager setSharingActivityChaptersDTO:];
-[DSNavigationManager setSharingActivityNavigationOrder:];
-[DSNavigationManager setSharingActivityNavigationOrderDTO:];
-[DSNavigationManager sharingActivityChapters];
-[DSNavigationManager sharingActivityChaptersDTO];
-[DSNavigationManager sharingActivityNavigationOrder];
-[DSNavigationManager sharingActivityNavigationOrderDTO];
-[DSNavigationManager shouldIngestURL:];
-[DSNavigationManager startingClassForURL:];
-[DSNavigationManager topViewControllerForUnorderedClass:];
```
