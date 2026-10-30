# `UIUserNotificationAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _authenticationRequired;
B _destructive;
@"NSString" _activationModeString;
@"NSString" _behaviorString;
@"NSString" _identifier;
@"NSString" _title;
Q _behavior;
@"NSDictionary" _parameters;
Q _activationMode;
```

## Properties

```
@property (T@"NSString",C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_title) title;
@property (TQ,N,V_behavior) behavior;
@property (T@"NSDictionary",C,N,V_parameters) parameters;
@property (TQ,N,V_activationMode) activationMode;
@property (TB,N,GisAuthenticationRequired,V_authenticationRequired) authenticationRequired;
@property (TB,N,GisDestructive,V_destructive) destructive;
@property (T@"NSString",R,N,V_activationModeString) activationModeString;
@property (T@"NSString",R,N,V_behaviorString) behaviorString;
```

## Class methods

```
+[UIUserNotificationAction supportsSecureCoding];
```

## Instance methods

```
-[UIUserNotificationAction setAuthenticationRequired:];
-[UIUserNotificationAction parameters];
-[UIUserNotificationAction mutableCopyWithZone:];
-[UIUserNotificationAction identifier];
-[UIUserNotificationAction setParameters:];
-[UIUserNotificationAction init];
-[UIUserNotificationAction setIdentifier:];
-[UIUserNotificationAction setBehavior:];
-[UIUserNotificationAction behavior];
-[UIUserNotificationAction activationMode];
-[UIUserNotificationAction title];
-[UIUserNotificationAction encodeWithCoder:];
-[UIUserNotificationAction isDestructive];
-[UIUserNotificationAction hash];
-[UIUserNotificationAction description];
-[UIUserNotificationAction isAuthenticationRequired];
-[UIUserNotificationAction initWithCoder:];
-[UIUserNotificationAction setTitle:];
-[UIUserNotificationAction setActivationMode:];
-[UIUserNotificationAction copyWithZone:];
-[UIUserNotificationAction setDestructive:];
-[UIUserNotificationAction isEqual:];
-[UIUserNotificationAction validatedAction];
-[UIUserNotificationAction activationModeString];
-[UIUserNotificationAction behaviorString];
-[UIUserNotificationAction initWithIdentifier:title:behavior:parameters:activationMode:isAuthenticationRequired:isDestructive:];
```
