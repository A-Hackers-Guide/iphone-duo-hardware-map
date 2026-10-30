# `_UIDocumentPickerNSURLWrapper`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 10 instance methods, 6 class methods

## Instance variables

```
@"NSURL" _url;
@"NSURL" _promiseURL;
@"NSData" _scope;
@"NSData" _promiseScope;
```

## Properties

```
@property (T@"NSURL",C,N,V_url) url;
@property (T@"NSURL",&,V_promiseURL) promiseURL;
@property (T@"NSData",&,V_scope) scope;
@property (T@"NSData",&,V_promiseScope) promiseScope;
```

## Class methods

```
+[_UIDocumentPickerNSURLWrapper supportsSecureCoding];
+[_UIDocumentPickerNSURLWrapper wrapperWithURL:readonly:];
+[_UIDocumentPickerNSURLWrapper assembleURL:sandbox:physicalURL:physicalSandbox:];
+[_UIDocumentPickerNSURLWrapper wrapperWithURL:];
+[_UIDocumentPickerNSURLWrapper wrapperForExportWithURL:error:];
+[_UIDocumentPickerNSURLWrapper wrapperWithURL:createSandboxIfNoneAttached:];
```

## Instance methods

```
-[_UIDocumentPickerNSURLWrapper scope];
-[_UIDocumentPickerNSURLWrapper encodeWithCoder:];
-[_UIDocumentPickerNSURLWrapper initWithCoder:];
-[_UIDocumentPickerNSURLWrapper setUrl:];
-[_UIDocumentPickerNSURLWrapper setScope:];
-[_UIDocumentPickerNSURLWrapper url];
-[_UIDocumentPickerNSURLWrapper promiseURL];
-[_UIDocumentPickerNSURLWrapper setPromiseURL:];
-[_UIDocumentPickerNSURLWrapper promiseScope];
-[_UIDocumentPickerNSURLWrapper setPromiseScope:];
```
