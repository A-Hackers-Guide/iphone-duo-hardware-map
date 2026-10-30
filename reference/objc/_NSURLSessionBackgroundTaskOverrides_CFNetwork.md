# `_NSURLSessionBackgroundTaskOverrides`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
C __allowsCellularAccess;
C __allowsExpensiveNetworkAccess;
C __allowsConstrainedNetworkAccess;
C __requiresPowerPluggedIn;
```

## Properties

```
@property (TC,V__allowsCellularAccess) _allowsCellularAccess;
@property (TC,V__allowsExpensiveNetworkAccess) _allowsExpensiveNetworkAccess;
@property (TC,V__allowsConstrainedNetworkAccess) _allowsConstrainedNetworkAccess;
@property (TC,V__requiresPowerPluggedIn) _requiresPowerPluggedIn;
@property (TB) allowsCellularAccess;
@property (TB) allowsExpensiveNetworkAccess;
@property (TB) allowsConstrainedNetworkAccess;
@property (TB) requiresPowerPluggedIn;
```

## Class methods

```
+[_NSURLSessionBackgroundTaskOverrides supportsSecureCoding];
```

## Instance methods

```
-[_NSURLSessionBackgroundTaskOverrides _requiresPowerPluggedIn];
-[_NSURLSessionBackgroundTaskOverrides setRequiresPowerPluggedIn:];
-[_NSURLSessionBackgroundTaskOverrides setAllowsExpensiveNetworkAccess:];
-[_NSURLSessionBackgroundTaskOverrides allowsExpensiveNetworkAccess];
-[_NSURLSessionBackgroundTaskOverrides requiresPowerPluggedIn];
-[_NSURLSessionBackgroundTaskOverrides allowsCellularAccess];
-[_NSURLSessionBackgroundTaskOverrides set_allowsCellularAccess:];
-[_NSURLSessionBackgroundTaskOverrides set_requiresPowerPluggedIn:];
-[_NSURLSessionBackgroundTaskOverrides _allowsCellularAccess];
-[_NSURLSessionBackgroundTaskOverrides setAllowsCellularAccess:];
-[_NSURLSessionBackgroundTaskOverrides allowsConstrainedNetworkAccess];
-[_NSURLSessionBackgroundTaskOverrides setAllowsConstrainedNetworkAccess:];
-[_NSURLSessionBackgroundTaskOverrides encodeWithCoder:];
-[_NSURLSessionBackgroundTaskOverrides _allowsConstrainedNetworkAccess];
-[_NSURLSessionBackgroundTaskOverrides description];
-[_NSURLSessionBackgroundTaskOverrides initWithCoder:];
-[_NSURLSessionBackgroundTaskOverrides set_allowsConstrainedNetworkAccess:];
-[_NSURLSessionBackgroundTaskOverrides set_allowsExpensiveNetworkAccess:];
-[_NSURLSessionBackgroundTaskOverrides _allowsExpensiveNetworkAccess];
```
