---
title: "10 Cool Things in Rails 2.3"
date: 2009-03-30 14:00:00 +0000
external-url: http://railspikes.com/2009/3/30/10-cool-things-in-rails-23
hash: bf8ed98019a7ba92ec4c669b34dceb4b
year: 2009
month: 03
scheme: http
host: railspikes.com
path: /2009/3/30/10-cool-things-in-rails-23

---

This was presented to the Ruby Users of Minnesota on March 30, 2009.



Here’s a quick look at 10 new Rails features that I think are cool. Not all of them are huge new features, but instead help solve annoying problems. I’ve also created a simple application that demonstrates most of these features. You can get it at BitBucket



10 Cool Things About Rails 2.3<object height="355" width="425"><param /><param /><param /><embed src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=10coolthingsaboutrails2-3-090329160723-phpapp01&#38;stripped_title=10-cool-things-about-rails-23" height="355" width="425"></embed></object>View more presentations from lukefrancl.

1. Rails Boots Faster in Development Mode


This is something all Rails developers can appreciate. In development mode, Rails now lazy loads as much as possible so that the server starts up much faster.



This is so fast, instead of replying on reloading (which doesn’t pick up changes to gems, lib directory, etc) one developer wrote a script (does anyone have the link for this?) that watches for file system changes and restarts your script/server process.



Using an empty Rails app, I got the following (totally non-scientific) real times for time script/server -d:



Rails 2.2: 1.461s
Rails 2.3: 0.869s



Presumably this difference would grow as more libraries were used, because Rails 2.3 will lazy load them. However I was too lazy to build up equivalent Rails 2.2 and 2.3 applications to try that out.



2. Rails Engines Officially Supported


Inspired by Merb’s slices implementation, Rails added official support for Engines, which are self-contained Rails apps that you can install into another application. Engines can have their own models, controllers, and views, and add their own routes.



Previously this was possible using the Engines plugin, but Engines would often break between Rails versions. Now that they are officially supported, this should be less frequent.



There are still some features from the unofficial Engines plugin that are not part of Rails core. You can read about that at the Rails Engines site.



3. Routing Improvements


RESTful routes now use less memory because formatted_* routes are no longer generated, resulting in a 50% memory savings.



Given this route:



map.resources :users



If you want to access the XML formatted version of a user resource, you would use:



user_path(123, :format => 'xml')



In Rails 2.3, :only and :except options to map.resources are not passed down to nested routes. The previous behavior was rather confusing so I think this is a good change.




  1
2
3
4

  map.resources :users, :only => [:index, :new, :create] do |user|
  # now will generate all the routes for hobbies
  user.resources :hobbies
end




4. JSON Improvements


ActiveSupport::JSON has been improved.



to_json will always quote keys now, per the JSON spec.



Before:



{123 => 'abc'}.to_json
=> '{123: "abc"}'



Now:



{123 => 'abc'}.to_json
=> '{"123": "abc"}'



Escaped Unicode characters will now be unescaped.



Before:



ActiveSupport::JSON.decode("{'hello': 'fa\\u00e7ade'}")
=> {"hello"=>"fa\\u00e7ade"}



Now:



ActiveSupport::JSON.decode("{'hello': 'fa\u00e7ade'}")
=> {"hello"=>"façade"}



See ticket 11000 for details.



5. Default scopes


Prior to Rails 2.3, if you executed a find without any options, you’d get the objects back unordered (technically, the database does not guarantee a particular ordering, but it would typically be by primary key, ascending).



Now, you can define the default sort and filtering options for finding models. The default scope works just like a named scope, but is used by default.




  1
2
3

  class User < ActiveRecord::Base
  default_scope :order => '`users`.name asc'
end




The default options can always be overridden using a custom finder.



User.all                                      # will use default scope
User.all(:order => 'name desc') # will use passed in order option.



Example:




  1
2
3
4
5
6
7
8
9

  User.create(:name => 'George')
User.create(:name => 'Bob')
User.create(:name => 'Alice')

puts User.all.map { |u| "#{u.id} - #{u.name}" }

3 - Alice
2 - Bob
1 - George




Note how the default order is respected.



6. Nested Transactions


Pass :requires_new => true to ActiveRecord::Base.transaction and a nested transaction will be created.




  1
2
3
4
5
6
7

  User.transaction do
  user1 = User.create(:name => "Alice")

  User.transaction(:requires_new => true) do
    user2 = User.create(:name => "Bob")
   end
end




This is actually emulated using save points because most databases do not support nested transactions. Some databases (SQLite) don’t support either save points or nested transactions, so in that case this works
just like Rails 2.2 where the inner transaction(s) have no effect and if there are any exceptions the entire transaction is rolled back.



7. Asset Host Objects


Since Rails 2.1, you could configure Rails to use an asset_host that was a Proc with two arguments, source and request.



For example, some browsers complain if an SSL request loads images from a non-secure source. To make sure SSL always loads from the same host, you could write this (from the documentation):




  1
2
3
4
5
6
7

  ActionController::Base.asset_host = Proc.new { |source, request|
  if request.ssl?
    "#{request.protocol}#{request.host_with_port}"
  else
    "#{request.protocol}assets.example.com"
  end
}




This works but it’s kind of messy and it’s difficult to implement complicated logic. Rails 2.3 allows you to implement the logic in an object that responds to call with one or two parameters, like the
Proc.



The above Proc could be implemented like this:




  1
2
3
4
5
6
7
8
9
10
11

  class SslAssetHost
  def call(source, request)
    if request.ssl?
      "#{request.protocol}#{request.host_with_port}"
    else
      "#{request.protocol}assets.example.com"
    end
  end
end

ActionController::Base.asset_host = SslAssetHost.new




David Heinemeier Hansson has already created a better plugin that handles this case: asset-hosting-with-minimum-ssl. It takes into account the peculiarities of the different browsers to use SSL as little as possible, reducing load on your server.



8. Easily update Rails timestamp fields


If you’ve ever wanted to update Rails’ automatic timestamp fields created_at or updated_at you’ve noticed how painful it can be. Rails REALLY didn’t want you to change those fields.



Not any more!



Now you can easily change created_at and updated_at:




  1
2
3
4

  
User.create(:name => "Alice", :created_at => 3.weeks.ago, :updated_at => 2.weeks.ago)

=> #<User id: 3, name: "Alice", created_at: "2009-03-08 00:06:58", updated_at: "2009-03-15 00:06:58">




Remember, If you don’t want your users changing these fields, you should make them attr_protected.



9. Nested Attributes and Forms


This greatly simplifies complex forms that deal with multiple objects.



First, nested attributes allow a parent object to delegate assignment to its child objects.




  1
2
3
4
5
6
7
8
9
10

  
class User < ActiveRecord::Base
 has_many :hobbies, :dependent => :destroy

  accepts_nested_attributes_for :hobbies
end

User.create(:name => 'Stan', 
            :hobbies_attributes => [{:name => 'Water skiing'},
                                    {:name => 'Hiking'}])




Nicely, this will save the parent and its associated models together and if there are any errors, none of the objects will be saved.



Forms with complex objects are now straight-forward. To use this in your forms, use the FormBuilder instance’s fields_for method.




  1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

  <% form_for(@user) do |f| %>
  <div>
    <%= f.label :name, "User name:" %>
    <%= f.text_field :name %>
  </div>

  <div>
    <h2>Hobbies</h2>

    <% f.fields_for(:hobbies) do |hf| %>
      <div>
  <%= hf.label :name, "Hobby name:" %>
  <%= hf.text_field :name %>
      </div>
      <% end %>
  </div>

  <%= f.submit 'Create' %>
<% end %>




One catch is that a form is displayed for every associated object. New objects obviously have no associations so you have to create a dummy object in your controller.




  1
2
3
4
5
6
7
8
9
10

  class UsersController < ApplicationController
  def new
    # In this contrived example, I create 3 dummy objects so I'll get
    # 3 blank form fields.
    @user = User.new
    @user.hobbies.build
    @user.hobbies.build
    @user.hobbies.build
  end
end




There are a lot of options for nested forms including deleting associated objects, so be sure to read the documentation. Ryan Daigle also has a great write-up.



10. Rails Metal \m/


You can now write very simple Rack endpoints for highly trafficked routes, like an API. These are slotted in before Rails picks up the route.



A Metal endpoint is any class that conforms to the Rack spec (i.e., it has a call method that takes an environment and returns the an array of status code, headers, and content).



Put your class in app/metal (not generated by default). Return a 404 response code for any requests you don’t want to handle. These will get passed on to Rails.



There’s a generator you can use to create an example Metal end point:



script/generate metal classname



In my sample app, I have what I would consider the “minimally useful” Rails Metal endpoint. It responds to /users.js and returns the list of users as JSON.




  1
2
3
4
5
6
7
8
9
10
11

  class UsersApi
  def self.call(env)
    # if this path was /users.js, reply with the list of users
    if env['PATH_INFO'] =~ /^\/users.js/
      [200, {'Content-Type' => 'application/json'}, User.all.to_json]
    else
      # otherwise, bail out with a 404 and let Rails handle the request
      [404, {'Content-Type' => 'text/html'}, 'not found']
    end
  end
end




If you want a little bit more help, you can use any other Rack-based framework, for example Sinatra.



For more details on how Rails Metal works, check out Jesse Newland’s article about it.



Thanks for reading! For more details about new features in Rails 2.3, read the excellent release notes

          
