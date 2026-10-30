# `WFAssociationContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _secondaryScanCompleted;
Q _state;
Q _originator;
@"NSString" _sectionNameJoined;
@"NSDictionary" _sectionCounts;
@"NSObject<WFNetworkListRecord>" _network;
@"NSDate" _associationStart;
```

## Properties

```
@property (T@"NSDate",&,N,V_associationStart) associationStart;
@property (TQ,N,V_state) state;
@property (TQ,N,V_originator) originator;
@property (T@"NSString",R,N) stateDescription;
@property (T@"NSString",R,N) originatorDescription;
@property (TB,N,V_secondaryScanCompleted) secondaryScanCompleted;
@property (T@"NSString",C,N,V_sectionNameJoined) sectionNameJoined;
@property (T@"NSDictionary",C,N,V_sectionCounts) sectionCounts;
@property (T@"NSObject<WFNetworkListRecord>",&,N,V_network) network;
```

## Instance methods

```
-[WFAssociationContext networkName];
-[WFAssociationContext setState:];
-[WFAssociationContext network];
-[WFAssociationContext setOriginator:];
-[WFAssociationContext initWithNetwork:];
-[WFAssociationContext stateDescription];
-[WFAssociationContext description];
-[WFAssociationContext originator];
-[WFAssociationContext state];
-[WFAssociationContext setNetwork:];
-[WFAssociationContext formattedStartDate];
-[WFAssociationContext associationStart];
-[WFAssociationContext originatorDescription];
-[WFAssociationContext secondaryScanCompleted];
-[WFAssociationContext sectionCounts];
-[WFAssociationContext sectionNameJoined];
-[WFAssociationContext setAssociationStart:];
-[WFAssociationContext setSecondaryScanCompleted:];
-[WFAssociationContext setSectionCounts:];
-[WFAssociationContext setSectionNameJoined:];
```
