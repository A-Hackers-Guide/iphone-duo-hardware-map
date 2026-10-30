# `CAFPairedDevice`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
C _state;
S _sortOrder;
@"NSString" _identifier;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSString",R,C,N,V_name) name;
@property (TS,R,N,V_sortOrder) sortOrder;
@property (TC,R,N,V_state) state;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
```

## Instance methods

```
-[CAFPairedDevice sortOrder];
-[CAFPairedDevice initWithDictionary:];
-[CAFPairedDevice identifier];
-[CAFPairedDevice description];
-[CAFPairedDevice name];
-[CAFPairedDevice state];
-[CAFPairedDevice dictionaryRepresentation];
-[CAFPairedDevice initWithIdentifier:name:sortOrder:state:];
```
