---
title: "10 Useful WordPress Coding Techniques"
date: 2009-10-26 04:21:17 +0000
external-url: http://www.smashingmagazine.com/2009/10/20/10-useful-wordpress-hacks-for-advanced-themes/
hash: db2dba4d486c58b397c84e7d1e6f865f
year: 2009
month: 10
scheme: http
host: www.smashingmagazine.com
path: /2009/10/20/10-useful-wordpress-hacks-for-advanced-themes/

---





      
        
    





10 Useful WordPress Coding Techniques (via @smashingmag) -

Since last year, the WordPress themes market has grown incredibly. The reason? Great designs, of course, but also a lot of amazing new functionality. Top WordPress developers are always looking to get the most out of WordPress and use all of their knowledge to find ways to make their favorite blogging engine even more powerful.

In this article, we have compiled 10 useful WordPress code snippets, hacks and tips to help you create a WordPress theme that stands out from the crowd.

You may be interested in the following related posts:


Power Tips For WordPress Template Developers
10 Useful WordPress Loop Hacks
Custom Field Hacks For WordPress
Mastering WordPress Shortcuts

1. Style Posts Individually


The problem.
Your blog has a lot of posts, but the posts aren’t all of the same type. To give special styling to one or more of your posts, you can take advantage of both the post_class() function and the post ID.

The solution.
To apply this trick, just open your single.php file, find the loop and replace it with the following:

<?php if (have_posts()) : ?>
<?php while (have_posts()) : the_post(); ?>
<div <?php post_class() ?> id="post-<?php the_ID(); ?>">
<h3><a href="<?php the_permalink() ?>"><?php the_title(); ?></a></h3>
<?php the_content(); ?>
</div>
<?php endwhile; else: ?>
<?php _e('Sorry, no posts matched your criteria.'); ?>
<?php endif; ?>
Code explanation.
The important part is mostly in line 3. Here, we have added the PHP post_class() function. Introduced in WordPress 2.8, this function adds CSS classes to the post. For example, it can add:


.hentry
.sticky
.category-tutorials
.tag-wordpress

With these CSS classes now added, you can now give a custom style to all posts that have the sticky tag or those that belong to the tutorials category.

The other important piece of this code is id="post-<?php the_ID(); ?>". By displaying the ID of the post here, we’re able to style a particular post. As an example:

#post-876{
background:#ccc;
}
Source:


Take advantage of the new post class

2. Display Related Posts… With Thumbnails!


The problem.
After they have read your latest post, what do your readers do? That’s easy: most of them simply leave. A great way to keep them interested is to display a list of related posts. Many plug-ins can do that, but for those who like to know how things works, here is some nice code to get related posts and their thumbnails.

The solution.
Simply paste this code after the the_content() function in your single.php file:

<?php
$original_post = $post;
$tags = wp_get_post_tags($post->ID);
if ($tags) {
  echo '<h2>Related Posts</h2>';
  $first_tag = $tags[0]->term_id;
  $args=array(
    'tag__in' => array($first_tag),
    'post__not_in' => array($post->ID),
    'showposts'=>4,
    'caller_get_posts'=>1
   );
  $my_query = new WP_Query($args);
  if( $my_query->have_posts() ) {
    echo "<ul>";
    while ($my_query->have_posts()) : $my_query->the_post(); ?>
      <li><img src="<?php bloginfo('template_directory'); ?>/timthumb/timthumb.php?src=<?php echo get_post_meta($post->ID, "post-img", true); ?>&h=40&w=40&zc=1" alt="" /><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title_attribute(); ?>"><?php the_title(); ?></a></li>
    <?php endwhile;
    echo "</ul>";
  }
}
$post = $original_post;
wp_reset_query();
?>

Code explanation.
First, this code makes use of TimbThumb, a PHP image-resizing script. We have used it to automatically resize images to 40 by 40 pixels.

Once this code is pasted in your theme, it uses the first tag of the post to fetch related posts. In this example, four related posts are displayed. You can change this number on line 10.

Also, notice that I have cloned the $post variable at the beginning of the script and restored it at the end. This prevents problems that may occur with the loop, such as comments being assigned to the wrong post.

Source:


How to: Show related posts without a plug-in

3. Alternate Post Styling On Your Home Page


The problem.
Many new WordPress themes have an amazing way of displaying posts on the home page. For example, we can display the first three posts bigger than the rest, with images and extended text, with the remaining posts shown more simply.

I have seen many themes in which developers use two distinct loops to achieve this, which isn’t necessary and can cause further problems. Let’s use a much simpler method.

The solution.
Here is a custom loop that displays the first three posts different than the rest. You can replace the existing loop in your index.php file with this code.

<?php
$postnum = 0;
while (have_posts()) : the_post(); ?>

<?php if ($postnum <= 3){ ?>
<div <?php post_class() ?> id="post-<?php the_ID(); ?>">
  <div class="date"><span><?php the_time('M j') ?></span></div>
    <h2>(<?php echo $postnum;?>)<a href="<?php the_permalink() ?>"><?php the_title(); ?></a></h2>
<div class="post-image" style="text-align:center;">
<a href="<?php the_permalink() ?>"><img src="<?php bloginfo('template_directory' ); ?>/timthumb.php?src=<?php  echo catch_that_image(); ?>&amp;w=500&amp;h=200&amp;zc=1" alt="<?php the_title(); ?>" /></a>
</div>
<p><?php the_content('Read the rest of this entry &raquo;'); ?></p>
<p class="more"><a href="#">Read More</a></p>
  </div>
</div>

<?php } else {
<div <?php post_class( 'single ' . $end ); ?> id="post-<?php the_ID(); ?>">
<div class="post-content">
<h3><a href="<?php the_permalink() ?>">(<?php echo $postnum; ?>)<?php the_title(); ?></a> <?php edit_post_link('_', '', ''); ?></h3>
<p><?php the_excerpt( '' ); ?></p>
<p class="more"><a href="#">Read More ?</a></p>
</div>
</div><!-- End post -->

<?php }
endwhile;
?>

Code explanation.
Nothing hard here! We just created a PHP variable, named $postnum, which is invoked at the end of the loop. If $postnum is less than or equal to 3, the post is displayed in full. Otherwise, it is displayed in its more compact form.

4. Using Multiple Loops


The problem.
When coding complex WordPress pages with more than one loop, it can happen that one of the loops doesn’t behave as expected: for example, unwanted offset, repeated posts, etc. Happily, with a bit of knowledge and a very useful function, we can avoid this.

The solution.
The following example features two distinct loops. Notice the rewind_posts() function on line 8. This example can be used on any WordPress file as is: index.php, single.php, etc.

// First loop (get the last 3 posts in the "featured" category)
<?php query_posts('category_name=featured&showposts=3'); ?>
<?php while (have_posts()) : the_post(); ?>
  <!-- Do stuff... -->
<?php endwhile;?>

//loop reset
<?php rewind_posts(); ?>

//Second loop (Get all posts)
<?php while (have_posts()) : the_post(); ?>
  <!-- Do stuff... -->
<?php endwhile; ?>

Code explanation.
This piece of code doesn’t use any hacks; rewind_posts() is a standard WordPress function.

The purpose of rewind_posts() is to “clear” a loop that has been previously used (like the first loop in our example above), allowing you to use a second loop that isn’t affected by the first loop’s results.

Source:


Multiple WordPress Loops Explained

5. Overwrite Post Titles Easily


The problem.
the_title() is a basic but very useful WordPress function: it displays the post or page’s title. No more, no less. But hey, have you ever wished you were able to display the full title in your listing of posts and a custom title on the actual post’s page? If so, find out how right here.

The solution.
In your single.php file, find the call to the the_title() function and replace it with the following code:

<?php $title = get_post_meta($post->ID, "custom-title", true);
if ($title != "") {
echo "<h1>".$title."</h1>";
} else { ?>
<h1><?php the_title(); ?></h1>
<?php } ?>

Once that’s done, you can rewrite the post’s title by creating a field named custom-title. Its value will be your custom title for this post.

Code explanation.
When this code loads, it retrieves the meta field named custom-title. If this meta field exists and isn’t blank, it is displayed as the post’s title. Otherwise, the the_title() function is called, and the post’s regular title is displayed.

Source:


Allow title overwrite on your WordPress blog

6. Add Multiple Sidebars


The problem.
Sidebars are great because they allow you to display a lot of useful info, such as related posts, author info, a blog roll, 125×125-pixel ad spaces and so on. But sidebars can quickly become very busy, and readers may be hard-pressed to find what they’re looking for. So, what about having different sidebars available and displaying the most appropriate one for the post?

The solution.
To apply this hack, duplicate your sidebar.php file and fill it with whatever information you would like to appear. Save the file as sidebar-whatever.php.

Once that’s done, open your single.php* file and find the call to the get_sidebar() function:

<?php get_sidebar(); ?>

Replace it with:

<?php $sidebar = get_post_meta($post->ID, "sidebar", true);
get_sidebar($sidebar);
?>

Now when you write a post, create a custom field named sidebar. Set its value as the name of the sidebar that you want to include. For example, if its value is right, WordPress will automatically include sidebar-right.php as a sidebar. 
If no custom sidebar field is found, WordPress automatically includes the default sidebar.

*The same can be done with page.php.

Code explanation.
This trick is quite simple. The first thing we did was look for a custom field named sidebar and get its value as a variable. Then, the variable is used as a parameter for the WordPress function get_sidebar(), which allows us to specify a particular file to use as a sidebar.

Source:


WordPress hack: Choose the sidebar to use, post by post

7. Display Content Only To Registered Users


The problem.
As you probably know, WordPress lets you decide whether to allow readers to create accounts and sign in to your blog. If you want to increase your blog’s registered readers or would just like to reward existing readers, why not keep some content private, just for them?

The solution.
To achieve this hack, we’ll use a shortcode. The first step is to create it. Open your functions.php file and paste the following code:

function member_check_shortcode($atts, $content = null) {
  if (is_user_logged_in() && !is_null($content) && !is_feed()) {
    return $content;
  } else {
    return 'Sorry, this part is only available to our members. Click here to become a member!';
}

add_shortcode('member', 'member_check_shortcode');

Once that’s done, you can add the following to your posts to create a section or text (or any other content) that will be displayed only to registered users:

[member]
This text will be displayed only to registered users.
[/member]

That’s it. Registered users will see the text contained in the shortcode, while unregistered users will see a message asking them to register.

Code explanation.
The first thing we’ve done is create a function named member_check_shortcode, which checks whether the current user is logged in. If they are, then the text contained in the [member] shortcode is displayed. Otherwise, the message on line 5 is shown.

If you’d like to know more about WordPress shortcodes, you should definitely have a look at our Mastering WordPress Shortcodes post.

Source:


Using shortcodes to show members-only content
WordPress shortcode: Display content to registered users only

8. Display Your Most Popular Content In The Sidebar


The problem.
If you want to feature your best content and help readers discover more articles from your blog, you might want to display a list of your most popular posts, based on the number of comments they’ve received, in your sidebar.

The solution.
This code is really easy to implement. Just paste it wherever you’d like your popular posts to appear. To get more or less than five posts, just change the value of the SQL limit clause on line 3.

<h2>Popular Posts</h2>
<ul>
<?php $result = $wpdb->get_results("SELECT comment_count,ID,post_title FROM $wpdb->posts ORDER BY comment_count DESC LIMIT 0 , 5");
foreach ($result as $post) {
setup_postdata($post);
$postid = $post->ID;
$title = $post->post_title;
$commentcount = $post->comment_count;
if ($commentcount != 0) { ?>
<li><a href="<?php echo get_permalink($postid); ?>" title="<?php echo $title ?>">

<?php echo $title ?></a> {<?php echo $commentcount ?>}</li>
<?php } } ?>
</ul>

Code explanation.
In this code, we use the $wpdb object to send a custom SQL query to the WordPress database. Then we verify that the results aren’t empty (i.e. that no posts are without comments), and finally we display the list of posts.

Sources


Create your own “Popular Posts” page
How to: Display your most popular content in your blog sidebar

9. Create A Drop-Down Menu For Easy Tag Navigation


The problem.
Tags are cool because they allow you to categorize content using precise terms. But displaying tag clouds is a problem: they are ugly, not easy to use and can be extremely big.

So, what’s the solution? Simply create a drop-down menu for your tags. That way, they don’t get in the way, but people still have easy access to them.

The solution.
To create our drop-down menu of tags, we first have to paste the two functions below into the functions.php file of our WordPress theme:

<?php
function dropdown_tag_cloud( $args = '' ) {
$defaults = array(
'smallest' => 8, 'largest' => 22, 'unit' => 'pt', 'number' => 45,
'format' => 'flat', 'orderby' => 'name', 'order' => 'ASC',
'exclude' => '', 'include' => ''
);
$args = wp_parse_args( $args, $defaults );

$tags = get_tags( array_merge($args, array('orderby' => 'count', 'order' => 'DESC')) ); // Always query top tags

if ( empty($tags) )
return;

$return = dropdown_generate_tag_cloud( $tags, $args ); // Here's where those top tags get sorted according to $args
if ( is_wp_error( $return ) )
return false;
else
echo apply_filters( 'dropdown_tag_cloud', $return, $args );
}

function dropdown_generate_tag_cloud( $tags, $args = '' ) {
global $wp_rewrite;
$defaults = array(
'smallest' => 8, 'largest' => 22, 'unit' => 'pt', 'number' => 45,
'format' => 'flat', 'orderby' => 'name', 'order' => 'ASC'
);
$args = wp_parse_args( $args, $defaults );
extract($args);

if ( !$tags )
return;
$counts = $tag_links = array();
foreach ( (array) $tags as $tag ) {
$counts[$tag->name] = $tag->count;
$tag_links[$tag->name] = get_tag_link( $tag->term_id );
if ( is_wp_error( $tag_links[$tag->name] ) )
return $tag_links[$tag->name];
$tag_ids[$tag->name] = $tag->term_id;
}

$min_count = min($counts);
$spread = max($counts) - $min_count;
if ( $spread <= 0 )
$spread = 1;
$font_spread = $largest - $smallest;
if ( $font_spread <= 0 )
$font_spread = 1;
$font_step = $font_spread / $spread;

// SQL cannot save you; this is a second (potentially different) sort on a subset of data.
if ( 'name' == $orderby )
uksort($counts, 'strnatcasecmp');
else
asort($counts);

if ( 'DESC' == $order )
$counts = array_reverse( $counts, true );

$a = array();

$rel = ( is_object($wp_rewrite) && $wp_rewrite->using_permalinks() ) ? ' rel="tag"' : '';

foreach ( $counts as $tag => $count ) {
$tag_id = $tag_ids[$tag];
$tag_link = clean_url($tag_links[$tag]);
$tag = str_replace(' ', '&nbsp;', wp_specialchars( $tag ));
$a[] = "\t<option value='$tag_link'>$tag ($count)</option>";
}

switch ( $format ) :
case 'array' :
$return =& $a;
break;
case 'list' :
$return = "<ul class='wp-tag-cloud'>\n\t<li>";
$return .= join("</li>\n\t<li>", $a);
$return .= "</li>\n</ul>\n";
break;
default :
$return = join("\n", $a);
break;
endswitch;

return apply_filters( 'dropdown_generate_tag_cloud', $return, $tags, $args );
}
?>

Once you’ve pasted this function in your functions.php file, you can use it to create your drop-down menu of tags. Just open the file where you want the list to be displayed and paste the following code:

<select name="tag-dropdown" onchange="document.location.href=this.options[this.selectedIndex].value;">
<option value="#">Liste d'auteurs</option>
<?php dropdown_tag_cloud('number=0&order=asc'); ?>

</select>
Code explanation.
To achieve this hack, we take the wp_tag_cloud() WordPress function and rewrite it to make it display tags in an HTML “Select” element.

Then, we just call the newly created dropdown_tag_cloud() in our theme to display the drop-down menu items.

Source:


Top 10 WordPress hacks from June ‘09

10. Auto-Resize Images Using TimThumb And WordPress Shortcodes


The problem.
A good blog post needs images, whether screenshots or simple eye-candy. Readers always prefer articles with nice pictures to plain boring text.

But images can be a pain to deal with, especially because of their various sizes. So how about we create a WordPress shortcode that uses Timthumb to automatically resize images?

The solution.
The first thing to do is create the shortcode. Paste the following code in your functions.php file:

function imageresizer( $atts, $content = null ) {
return '<img src="http://media2.smashingmagazine.com/wp-content/uploads/2009/10//timthumb/timthumb.php?src='.$content.'&w=590" alt="" />';
}

add_shortcode('img', 'imageresizer');
Now, you can use the following syntax to add an automatically resized image to your blog post:

[img]http://www.yoursite.com/yourimage.jpg[/img]
Code explanation.
You have probably already noticed how cool WordPress shortcodes are and how they make your blogging life easier. This code simply creates a shortcode that takes a single parameter: the image’s URL. Please notice that it’s not a good idea to resize large images this way as it unnecessarily increases the server load – in such cases it’s better to create and upload smaller images instead.

TimThumb resizes the image to 590 pixels wide, as specified on line 2 (w=590). Of course, you can change this value or add a height parameter (e.g. h=60).

Source:


Top 10 WordPress hacks from June ‘09

Related posts
You may be interested in the following related posts:


10 Handy WordPress Comments Hacks
Power Tips For WordPress Template Developers
10 Useful WordPress Loop Hacks
Custom Field Hacks For WordPress
15 Useful Twitter Hacks and Plugins For WordPress
Mastering WordPress Shortcuts

About the Author
This guest post was written by Jean-Baptiste Jung, a 27-year-old WordPress expert from the French-speaking part of Belgium. He blogs about WordPress at WpRecipes, about practical Web development tips at Cats Who Code and about blogging at Cats Who Blog. You can stay in touch with Jean by following him on Twitter.

(al)



© Jean-Baptiste Jung for Smashing Magazine, 2009. |
Permalink | 
70 comments | 
Add to del.icio.us | Digg this | Stumble on StumbleUpon! | Tweet it! | Submit to Reddit | Forum Smashing Magazine


Post tags: hacks, tricks, wordpress


