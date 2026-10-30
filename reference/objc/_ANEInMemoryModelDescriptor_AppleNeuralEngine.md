# `_ANEInMemoryModelDescriptor`

- Image: [`/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/AppleNeuralEngine`](../userland/System__Library__PrivateFrameworks__AppleNeuralEngine.framework__AppleNeuralEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 14 instance methods, 3 class methods

## Instance variables

```
B _isMILModel;
@"NSString" _networkTextHash;
@"NSString" _weightsHash;
@"NSString" _optionsPlistHash;
@"NSData" _networkText;
@"NSDictionary" _weights;
@"NSData" _optionsPlist;
@"NSDictionary" _perFileHashes;
```

## Properties

```
@property (T@"NSString",R,C,N,V_networkTextHash) networkTextHash;
@property (T@"NSString",R,C,N,V_weightsHash) weightsHash;
@property (T@"NSString",R,N,V_optionsPlistHash) optionsPlistHash;
@property (T@"NSData",R,C,N,V_networkText) networkText;
@property (T@"NSDictionary",R,N,V_weights) weights;
@property (T@"NSData",R,N,V_optionsPlist) optionsPlist;
@property (TB,R,N,V_isMILModel) isMILModel;
@property (T@"NSDictionary",R,N,V_perFileHashes) perFileHashes;
```

## Class methods

```
+[_ANEInMemoryModelDescriptor new];
+[_ANEInMemoryModelDescriptor modelWithNetworkDescription:weights:optionsPlist:];
+[_ANEInMemoryModelDescriptor modelWithMILText:weights:optionsPlist:];
```

## Instance methods

```
-[_ANEInMemoryModelDescriptor init];
-[_ANEInMemoryModelDescriptor hash];
-[_ANEInMemoryModelDescriptor isEqual:];
-[_ANEInMemoryModelDescriptor weights];
-[_ANEInMemoryModelDescriptor hexStringIdentifier];
-[_ANEInMemoryModelDescriptor networkTextHash];
-[_ANEInMemoryModelDescriptor initWithNetworkText:weights:optionsPlist:isMILModel:];
-[_ANEInMemoryModelDescriptor isEqualToInMemoryModelDescriptor:];
-[_ANEInMemoryModelDescriptor isMILModel];
-[_ANEInMemoryModelDescriptor networkText];
-[_ANEInMemoryModelDescriptor optionsPlist];
-[_ANEInMemoryModelDescriptor optionsPlistHash];
-[_ANEInMemoryModelDescriptor perFileHashes];
-[_ANEInMemoryModelDescriptor weightsHash];
```
