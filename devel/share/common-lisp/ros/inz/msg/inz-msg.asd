
(cl:in-package :asdf)

(defsystem "inz-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Formation" :depends-on ("_package_Formation"))
    (:file "_package_Formation" :depends-on ("_package"))
    (:file "PoseTwist" :depends-on ("_package_PoseTwist"))
    (:file "_package_PoseTwist" :depends-on ("_package"))
  ))