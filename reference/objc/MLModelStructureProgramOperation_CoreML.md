# `MLModelStructureProgramOperation`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSString" _operatorName;
@"NSDictionary" _inputs;
@"NSArray" _outputs;
@"NSArray" _blocks;
@"MLModelStructurePath" _path;
@"NSString" _milTextLocation;
@"NSNumber" _milId;
```

## Properties

```
@property (T@"MLModelStructurePath",R,N,V_path) path;
@property (T@"NSString",R,C,N,V_milTextLocation) milTextLocation;
@property (T@"NSNumber",R,C,N,V_milId) milId;
@property (T@"NSString",R,C,N,V_operatorName) operatorName;
@property (T@"NSDictionary",R,C,N,V_inputs) inputs;
@property (T@"NSArray",R,C,N,V_outputs) outputs;
@property (T@"NSArray",R,C,N,V_blocks) blocks;
```

## Instance methods

```
-[MLModelStructureProgramOperation outputs];
-[MLModelStructureProgramOperation inputs];
-[MLModelStructureProgramOperation operatorName];
-[MLModelStructureProgramOperation path];
-[MLModelStructureProgramOperation milTextLocation];
-[MLModelStructureProgramOperation blocks];
-[MLModelStructureProgramOperation initWithMILOperation:path:];
-[MLModelStructureProgramOperation initWithOperatorName:inputs:outputs:blocks:path:milTextLocation:milId:];
-[MLModelStructureProgramOperation milId];
```
