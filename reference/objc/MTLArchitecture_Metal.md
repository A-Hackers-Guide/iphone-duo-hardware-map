# `MTLArchitecture`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _revision;
i _cpuType;
i _cpuSubtype;
```

## Properties

```
@property (T@"NSString",R,V_revision) revision;
@property (Ti,R,V_cpuType) cpuType;
@property (Ti,R,V_cpuSubtype) cpuSubtype;
@property (T@"NSString",R,V_name) name;
```

## Instance methods

```
-[MTLArchitecture revision];
-[MTLArchitecture dealloc];
-[MTLArchitecture cpuSubtype];
-[MTLArchitecture initWithCPUType:cpuSubtype:revision:];
-[MTLArchitecture cpuType];
-[MTLArchitecture copyWithZone:];
-[MTLArchitecture initWithCPUType:cpuSubtype:];
-[MTLArchitecture name];
```
