# `CTAsciiAddress`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `CTMessageAddress`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _address;
```

## Properties

```
@property (T@"NSString",R,V_address) address;
```

## Class methods

```
+[CTAsciiAddress asciiAddressWithString:];
```

## Instance methods

```
-[CTAsciiAddress address];
-[CTAsciiAddress encodedString];
-[CTAsciiAddress initWithAddress:];
-[CTAsciiAddress copyWithZone:];
-[CTAsciiAddress canonicalFormat];
```
