# `MTLCounterSetInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLCounterSet`
- 3 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _description;
@"NSArray" _counters;
```

## Properties

```
@property (T@"NSString",R,C,V_name) name;
@property (T@"NSArray",R,C,V_counters) counters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLCounterSetInternal dealloc];
-[MTLCounterSetInternal hash];
-[MTLCounterSetInternal description];
-[MTLCounterSetInternal isEqual:];
-[MTLCounterSetInternal name];
-[MTLCounterSetInternal counters];
-[MTLCounterSetInternal initWithName:description:counters:];
```
