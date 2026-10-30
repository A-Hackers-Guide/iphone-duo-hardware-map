# `CAStateTransition`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSString" _fromState;
@"NSString" _toState;
@"NSArray" _elements;
```

## Properties

```
@property (T@"NSString",C,N,V_fromState) fromState;
@property (T@"NSString",C,N,V_toState) toState;
@property (T@"NSArray",C,N,V_elements) elements;
```

## Class methods

```
+[CAStateTransition supportsSecureCoding];
+[CAStateTransition CAMLParserStartElement:];
```

## Instance methods

```
-[CAStateTransition setElements:];
-[CAStateTransition CAMLTypeForKey:];
-[CAStateTransition setToState:];
-[CAStateTransition setFromState:];
-[CAStateTransition debugDescription];
-[CAStateTransition elements];
-[CAStateTransition CAMLParser:setValue:forKey:];
-[CAStateTransition init];
-[CAStateTransition dealloc];
-[CAStateTransition duration];
-[CAStateTransition encodeWithCAMLWriter:];
-[CAStateTransition fromState];
-[CAStateTransition encodeWithCoder:];
-[CAStateTransition initWithCoder:];
-[CAStateTransition copyWithZone:];
-[CAStateTransition toState];
```
