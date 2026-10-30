# `SAPersistenceManager`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SAPersistenceStore" _store;
@"SAPersistenceManagerSettings" _settings;
@"NSHashTable" _observers;
```

## Properties

```
@property (T@"SAPersistenceManagerSettings",&,V_settings) settings;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"SAPersistenceStore",R,N,V_store) store;
```

## Instance methods

```
-[SAPersistenceManager save];
-[SAPersistenceManager load];
-[SAPersistenceManager store];
-[SAPersistenceManager setSettings:];
-[SAPersistenceManager removeObserver:];
-[SAPersistenceManager settings];
-[SAPersistenceManager reset];
-[SAPersistenceManager addObserver:];
-[SAPersistenceManager setObservers:];
-[SAPersistenceManager observers];
-[SAPersistenceManager initWithSettings:];
-[SAPersistenceManager _createDirectoryIfNotPresent];
-[SAPersistenceManager _notifyObserversOnReadFromURL:bytes:];
-[SAPersistenceManager _notifyObserversOnWriteToURL:bytes:];
-[SAPersistenceManager onUpdatedMonitoringSessionRecord:];
```
