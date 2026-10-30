# `AUAudioUnit_XH`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnit_XPC`
- 5 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSExtension" _extension;
@"NSUUID" _requestIdentifier;
@"AUAudioUnit_XPC" _strongInstance;
@? _speechSynthesisOutputMetadataBlock;
@? _completionBlock;
```

## Properties

```
@property (T@"AUAudioUnit_XPC",&,N,V_strongInstance) strongInstance;
@property (T@?,C,N,V_completionBlock) completionBlock;
```

## Class methods

```
+[AUAudioUnit_XH instantiateWithExtension:componentDescription:instance:options:completionHandler:];
```

## Instance methods

```
-[AUAudioUnit_XH _internalInitWithExtension:componentDescription:instance:completion:];
-[AUAudioUnit_XH speechSynthesisOutputMetadataBlock];
-[AUAudioUnit_XH setCompletionBlock:];
-[AUAudioUnit_XH completionBlock];
-[AUAudioUnit_XH requestViewControllerWithCompletionHandler:];
-[AUAudioUnit_XH dealloc];
-[AUAudioUnit_XH strongInstance];
-[AUAudioUnit_XH _open:completion:];
-[AUAudioUnit_XH extension];
-[AUAudioUnit_XH setSpeechSynthesisOutputMetadataBlock:];
-[AUAudioUnit_XH setStrongInstance:];
```
