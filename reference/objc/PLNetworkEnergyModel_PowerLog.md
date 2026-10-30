# `PLNetworkEnergyModel`

- Image: [`/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`](../userland/System__Library__PrivateFrameworks__PowerLog.framework__PowerLog.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 30 instance methods, 0 class methods

## Instance variables

```
C _linkType;
I _updateCount;
d _powerlevel1Duration;
d _powerlevel2Duration;
d _powerlevel3Duration;
d _overallBytes;
d _overallDuration;
@"NSString" _taskUUID;
@"NSArray" _linkCost;
@"NSArray" _linkDuration;
@"NSArray" _linkLevel1Parameters;
```

## Properties

```
@property (Td,V_powerlevel1Duration) powerlevel1Duration;
@property (Td,V_powerlevel2Duration) powerlevel2Duration;
@property (Td,V_powerlevel3Duration) powerlevel3Duration;
@property (TC,V_linkType) linkType;
@property (Td,V_overallBytes) overallBytes;
@property (Td,V_overallDuration) overallDuration;
@property (TI,V_updateCount) updateCount;
@property (T@"NSString",&,V_taskUUID) taskUUID;
@property (T@"NSArray",&,V_linkCost) linkCost;
@property (T@"NSArray",&,V_linkDuration) linkDuration;
@property (T@"NSArray",&,V_linkLevel1Parameters) linkLevel1Parameters;
```

## Instance methods

```
-[PLNetworkEnergyModel linkType];
-[PLNetworkEnergyModel taskUUID];
-[PLNetworkEnergyModel updateCount];
-[PLNetworkEnergyModel setLinkType:];
-[PLNetworkEnergyModel description];
-[PLNetworkEnergyModel setUpdateCount:];
-[PLNetworkEnergyModel overallDuration];
-[PLNetworkEnergyModel computeLevel1TimeWithBytes:];
-[PLNetworkEnergyModel getEnergy];
-[PLNetworkEnergyModel initWithLinkType:];
-[PLNetworkEnergyModel initWithLinkType:withTaskUUID:];
-[PLNetworkEnergyModel linkCost];
-[PLNetworkEnergyModel linkDuration];
-[PLNetworkEnergyModel linkLevel1Parameters];
-[PLNetworkEnergyModel overallBytes];
-[PLNetworkEnergyModel powerlevel1Duration];
-[PLNetworkEnergyModel powerlevel2Duration];
-[PLNetworkEnergyModel powerlevel3Duration];
-[PLNetworkEnergyModel reportEnergyToPowerlogWithClientID:];
-[PLNetworkEnergyModel setLinkCost:];
-[PLNetworkEnergyModel setLinkDuration:];
-[PLNetworkEnergyModel setLinkLevel1Parameters:];
-[PLNetworkEnergyModel setOverallBytes:];
-[PLNetworkEnergyModel setOverallDuration:];
-[PLNetworkEnergyModel setPowerlevel1Duration:];
-[PLNetworkEnergyModel setPowerlevel2Duration:];
-[PLNetworkEnergyModel setPowerlevel3Duration:];
-[PLNetworkEnergyModel setTaskUUID:];
-[PLNetworkEnergyModel updateAllLevelTimesWithLevel1Time:withUpdateDuration:];
-[PLNetworkEnergyModel updateWithBytes:withDuration:];
```
