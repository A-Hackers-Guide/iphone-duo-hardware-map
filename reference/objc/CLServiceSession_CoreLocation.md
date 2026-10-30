# `CLServiceSession`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 8 instance methods, 7 class methods

## Instance variables

```
@? _clientCallback;
@"CLServiceSessionInternal" _serviceSessionInternal;
@"CLFullAccuracySession" _fullAccuracySession;
Q _serviceSessionDiagnosticMask;
Q _fullAccuracySessionDiagnosticMask;
Q _aggregatedDiagnosticMask;
q _authorizationRequirement;
@"NSString" _fullAccuracyPurposeKey;
```

## Class methods

```
+[CLServiceSession disconnectedSessionRequiringAuthorization:];
+[CLServiceSession disconnectedSessionRequiringAuthorization:fullAccuracyPurposeKey:];
+[CLServiceSession sessionRequiringAuthorization:];
+[CLServiceSession sessionRequiringAuthorization:fullAccuracyPurposeKey:];
+[CLServiceSession sessionRequiringAuthorization:fullAccuracyPurposeKey:queue:handler:];
+[CLServiceSession sessionRequiringAuthorization:queue:handler:];
+[CLServiceSession sessionWithLocationManager:authorizationRequirement:fullAccuracyPurposeKey:queue:handler:];
```

## Instance methods

```
-[CLServiceSession dealloc];
-[CLServiceSession setHandler:];
-[CLServiceSession invalidate];
-[CLServiceSession _serviceSessionInternal];
-[CLServiceSession handleDiagnosticUpdate];
-[CLServiceSession initDisconnectedSessionWithAuthorizationRequirement:fullAccuracyPurposeKey:];
-[CLServiceSession initWithLocationManager:authorizationRequirement:fullAccuracyPurposeKey:queue:handler:];
-[CLServiceSession setupSessionInternalWithLocationManager:authorizationRequirement:fullAccuracyPurposeKey:queue:];
```
