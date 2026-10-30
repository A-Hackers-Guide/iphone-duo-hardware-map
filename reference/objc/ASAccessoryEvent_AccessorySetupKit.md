# `ASAccessoryEvent`

- Image: [`/System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit`](../userland/System__Library__Frameworks__AccessorySetupKit.framework__AccessorySetupKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _eventType;
@"ASAccessory" _accessory;
@"NSError" _error;
```

## Properties

```
@property (T@"ASAccessory",C,N,V_accessory) accessory;
@property (T@"NSError",C,N,V_error) error;
@property (Tq,R,N,V_eventType) eventType;
```

## Class methods

```
+[ASAccessoryEvent supportsSecureCoding];
```

## Instance methods

```
-[ASAccessoryEvent setError:];
-[ASAccessoryEvent eventType];
-[ASAccessoryEvent descriptionWithLevel:];
-[ASAccessoryEvent error];
-[ASAccessoryEvent initWithEventType:];
-[ASAccessoryEvent description];
-[ASAccessoryEvent accessory];
-[ASAccessoryEvent setAccessory:];
-[ASAccessoryEvent initWithEventType:error:];
```
