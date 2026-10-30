# `SRElectrocardiogramSession`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 2 class methods

## Instance variables

```
q _state;
q _sessionGuidance;
@"NSString" _identifier;
```

## Properties

```
@property (Tq,R,N,V_state) state;
@property (Tq,R,N,V_sessionGuidance) sessionGuidance;
@property (T@"NSString",R,C,N,V_identifier) identifier;
```

## Class methods

```
+[SRElectrocardiogramSession supportsSecureCoding];
+[SRElectrocardiogramSession new];
```

## Instance methods

```
-[SRElectrocardiogramSession identifier];
-[SRElectrocardiogramSession init];
-[SRElectrocardiogramSession dealloc];
-[SRElectrocardiogramSession encodeWithCoder:];
-[SRElectrocardiogramSession hash];
-[SRElectrocardiogramSession description];
-[SRElectrocardiogramSession initWithCoder:];
-[SRElectrocardiogramSession copyWithZone:];
-[SRElectrocardiogramSession isEqual:];
-[SRElectrocardiogramSession state];
-[SRElectrocardiogramSession isEqualToSession:];
-[SRElectrocardiogramSession sessionGuidance];
-[SRElectrocardiogramSession initWithState:sessionGuidance:identifier:];
```
