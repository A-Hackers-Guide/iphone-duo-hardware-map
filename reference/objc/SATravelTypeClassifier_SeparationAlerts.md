# `SATravelTypeClassifier`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SATravelTypeClassifierServiceProtocol`
- 6 instance variables, 7 properties, 23 instance methods, 1 class methods

## Instance variables

```
Q _userActivityType;
Q _currentHints;
@"<SATimeServiceProtocol>" _clock;
@"NSHashTable" _clients;
Q _currentTravelType;
@"NSDate" _currentTravelTypeChangeDate;
```

## Properties

```
@property (T@"<SATimeServiceProtocol>",&,N,V_clock) clock;
@property (T@"NSHashTable",&,N,V_clients) clients;
@property (TQ,N,V_currentTravelType) currentTravelType;
@property (T@"NSDate",C,N,V_currentTravelTypeChangeDate) currentTravelTypeChangeDate;
@property (TQ,N,V_currentHints) currentHints;
@property (TQ,R,N) travelType;
@property (TQ,N,V_userActivityType) userActivityType;
```

## Class methods

```
+[SATravelTypeClassifier convertSATravelTypeToString:];
```

## Instance methods

```
-[SATravelTypeClassifier clients];
-[SATravelTypeClassifier clock];
-[SATravelTypeClassifier setClock:];
-[SATravelTypeClassifier ingestTAEvent:];
-[SATravelTypeClassifier removeClient:];
-[SATravelTypeClassifier setClients:];
-[SATravelTypeClassifier addClient:];
-[SATravelTypeClassifier setUserActivityType:];
-[SATravelTypeClassifier userActivityType];
-[SATravelTypeClassifier initWithClock:];
-[SATravelTypeClassifier setCurrentTravelTypeChangeDate:];
-[SATravelTypeClassifier _handleUserActivityEvent:];
-[SATravelTypeClassifier _handleVehicleStateEvent:];
-[SATravelTypeClassifier _notifyAllClientsOfHintsChangeFrom:to:];
-[SATravelTypeClassifier _notifyAllClientsOfTravelTypeChangeFrom:to:];
-[SATravelTypeClassifier _updateTravelState:withHints:];
-[SATravelTypeClassifier _vehicularHintsToString:];
-[SATravelTypeClassifier currentHints];
-[SATravelTypeClassifier currentTravelType];
-[SATravelTypeClassifier currentTravelTypeChangeDate];
-[SATravelTypeClassifier setCurrentHints:];
-[SATravelTypeClassifier setCurrentTravelType:];
-[SATravelTypeClassifier travelType];
```
