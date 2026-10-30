# `NeighborGraph`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _bssids;
@"NSMutableArray" _graph;
@"WAPersistentContainer" _persistentContainer;
@"NSMutableArray" _bssidsDwellTimes;
@"NSString" _ssid;
```

## Properties

```
@property (T@"NSArray",&,N,V_bssids) bssids;
@property (T@"NSMutableArray",&,N,V_graph) graph;
@property (T@"WAPersistentContainer",&,N,V_persistentContainer) persistentContainer;
@property (T@"NSMutableArray",&,N,V_bssidsDwellTimes) bssidsDwellTimes;
@property (T@"NSString",&,N,V_ssid) ssid;
```

## Instance methods

```
-[NeighborGraph graph];
-[NeighborGraph ssid];
-[NeighborGraph setSsid:];
-[NeighborGraph setPersistentContainer:];
-[NeighborGraph setGraph:];
-[NeighborGraph persistentContainer];
-[NeighborGraph bssids];
-[NeighborGraph setBssids:];
-[NeighborGraph setNeighborsForBssid:neighbors:];
-[NeighborGraph bssidsDwellTimes];
-[NeighborGraph copyNeighborGraphAsDictionaryOnMoc:];
-[NeighborGraph doesPathExist:target:];
-[NeighborGraph graphDensity];
-[NeighborGraph initWithBssidArray:ssid:persistentContainer:];
-[NeighborGraph setBssidsDwellTimes:];
-[NeighborGraph setNeighborsForBssid:dwellTime:neighborInfoArray:];
```
