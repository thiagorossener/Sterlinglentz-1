class PostsController < ApplicationController

  def index
    unless params[:title].blank?
      @posts = Refinery::Blog::Post.where(:title => params[:title])
    else
      @posts = Refinery::Blog::Post.all
    end

  end
end