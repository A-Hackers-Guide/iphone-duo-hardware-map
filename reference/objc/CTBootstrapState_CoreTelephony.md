# `CTBootstrapState`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
i _bootstrapStatus;
```

## Properties

```
@property (Ti,N,V_bootstrapStatus) bootstrapStatus;
```

## Class methods

```
+[CTBootstrapState supportsSecureCoding];
```

## Instance methods

```
-[CTBootstrapState encodeWithCoder:];
-[CTBootstrapState description];
-[CTBootstrapState initWithCoder:];
-[CTBootstrapState copyWithZone:];
-[CTBootstrapState isEqual:];
-[CTBootstrapState bootstrapStatus];
-[CTBootstrapState setBootstrapStatus:];
```
