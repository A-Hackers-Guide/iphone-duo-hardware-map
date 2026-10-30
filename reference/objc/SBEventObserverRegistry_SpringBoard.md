# `SBEventObserverRegistry`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
^v _provider;
@"NSMutableDictionary" _observers;
```

## Instance methods

```
-[SBEventObserverRegistry postEventToInterestedObservers:];
-[SBEventObserverRegistry addObserverWithToken:forEvent:];
-[SBEventObserverRegistry handleEvent:token:action:];
-[SBEventObserverRegistry removeObserverWithToken:forEvent:];
-[SBEventObserverRegistry setValue:forState:];
```
